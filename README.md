# Simple AI Chat
A simple AI chat using Ollama e Streamlit with Docker.

## Versions

Docker version 27.5.1
Python 3.13

## Running

Running containers: 
```bash
docker compose up -d
```

Pushing llama3.2 model:
```bash
docker exec -it ollama ollama pull llama3.2
```bash