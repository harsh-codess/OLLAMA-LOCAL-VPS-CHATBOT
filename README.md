# Ollama Chatbot

A Streamlit-based Q&A chatbot using Ollama models.

## Screenshots

### DeepSeek-R1 Model Demo
![DeepSeek Model Demo](assets/deepseek%20model.png)

### Mistral Model Demo
![Mistral Model Demo](assets/mistral%20model.png)

## Features
- Local LLM integration with Ollama
- Multiple model support (Mistral, DeepSeek-R1)
- Real-time chat interface
- Memory usage monitoring
- Error handling and status checks

## Model Comparison

| Model | RAM Required | Performance | Best For |
|-------|-------------|-------------|----------|
| **Mistral** | ~4GB | Fast, efficient | General chat, lower-end systems |
| **DeepSeek-R1** | ~5.4GB | Advanced reasoning | Complex tasks, coding, analysis |

## Deployment Options & Limitations

### ✅ **Local Development** (Recommended)
```bash
pip install -r requirements.txt
streamlit run app.py
```

### ✅ **Docker Local Deployment**
```bash
docker-compose up -d
```

### ✅ **VPS/Cloud Server with Docker**
- Requires: 8GB+ RAM, preferably GPU
- Install Docker & Docker Compose
- Run: `docker-compose up -d`

### ❌ **Streamlit Cloud / Heroku**
- **Not suitable**: These platforms don't support Ollama
- **Reason**: Ollama requires local model files and specific system resources

### ❌ **Serverless Platforms**
- **Not suitable**: AWS Lambda, Vercel, etc.
- **Reason**: Models are too large for serverless environments

## Alternative for Cloud Deployment

For true cloud deployment, consider modifying the app to use:
- OpenAI API
- Anthropic Claude API  
- Google Gemini API
- Azure OpenAI

## Best Deployment Strategy

1. **Development**: Run locally with Ollama
2. **Team Sharing**: Deploy on local network or VPS with Docker
3. **Production**: Consider cloud APIs for scalability

## Hardware Requirements

- **Minimum**: 8GB RAM, 10GB storage
- **Recommended**: 16GB RAM, SSD, GPU (optional)
