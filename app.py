import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
import os

import os
from dotenv import load_dotenv
load_dotenv()

## Langsmith Tracking
langchain_api_key = os.getenv("LANGCHAIN_API_KEY")
if langchain_api_key:
    os.environ["LANGCHAIN_API_KEY"] = langchain_api_key
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_PROJECT"] = "Simple Q&A Chatbot With Ollama"

## Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respond to the user queries"),
        ("user","Question:{question}")
    ]
)

def generate_response(question,llm,temperature,max_tokens):
    try:
        llm=Ollama(model=llm)
        output_parser=StrOutputParser()
        chain=prompt|llm|output_parser
        answer=chain.invoke({'question':question})
        return answer
    except Exception as e:
        if "OllamaEndpointNotFoundError" in str(type(e)):
            return "❌ Error: Ollama is not running. Please start Ollama first by running 'ollama serve' in your terminal."
        elif "more system memory" in str(e):
            return "❌ Error: Not enough RAM for this model. Try using 'mistral' instead, or close other applications to free up memory."
        else:
            return f"❌ Error: {str(e)}"

## Title of the app
st.title("Enhanced Q&A Chatbot With Ollama")

# Add deployment warning
st.info("🔧 **Deployment Note**: This app runs Ollama locally. For cloud deployment, consider using OpenAI API or other cloud LLM services.")

# Add setup instructions
with st.expander("📋 Setup Instructions", expanded=False):
    st.markdown("""
    **For Local Development:**
    
    1. **Install Ollama**: Download from [ollama.ai](https://ollama.ai)
    2. **Start Ollama Server**: 
       - Open **Command Prompt** and run: `ollama serve`
       - If you get "bind: Only one usage..." error, Ollama is already running ✅
    3. **Pull Models** (one-time setup): In command prompt, run:
       - `ollama pull mistral` (Lighter model, ~4GB RAM)
       - `ollama pull deepseek-r1` (Requires ~5.4GB RAM)
    4. **Check Status**: Use the button in the sidebar to verify connection
    
    **For Cloud Deployment:**
    - **Streamlit Cloud**: ❌ Not suitable (no Ollama support)
    - **Docker on VPS**: ✅ Possible but requires GPU/high RAM
    - **Local Network**: ✅ Best option for sharing with team
    
    **Memory Requirements:**
    - **mistral**: ~4GB RAM (Recommended for systems with 8GB or less)
    - **deepseek-r1**: ~5.4GB RAM (Requires 8GB+ system RAM)
    
    **Note**: If you get memory errors, try using mistral instead.
    """)

## Select the Ollama model
llm=st.sidebar.selectbox("Select Open Source model",["mistral", "deepseek-r1"], 
                        help="mistral: Lighter model (~4GB RAM)\ndeepseek-r1: More capable but requires more RAM (~5.4GB)")

## Adjust response parameter
temperature=st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

## Main interface for user input
st.write("Go ahead and ask any question")

# Add Ollama status check
with st.sidebar:
    st.markdown("---")
    st.markdown("**Ollama Status**")
    if st.button("Check Ollama Connection"):
        try:
            test_llm = Ollama(model="mistral")  # Test with lighter model
            test_llm.invoke("Hi")
            st.success("✅ Ollama is running and models are ready")
        except Exception as e:
            if "model 'mistral' not found" in str(e).lower():
                st.warning("⚠️ Ollama is running but 'mistral' model not found. Run: `ollama pull mistral`")
            elif "more system memory" in str(e):
                st.error("❌ Insufficient RAM. Close other applications or use a lighter model.")
            else:
                st.error("❌ Ollama connection failed. Make sure Ollama is installed and running.")

user_input=st.text_input("You:")

if user_input:
    with st.spinner("Generating response..."):
        response=generate_response(user_input,llm,temperature,max_tokens)
    st.write(response)
else:
    st.write("Please provide the user input")


