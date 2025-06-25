# Simple AI Chat
A simple AI chat using Ollama, Streamlit and Docker.

## Software Versions

| Software         | Version |
|------------------|---------|
| Docker           | 27.5.1  |
| Python           | 3.13    |
| streamlit        | 1.46.0  |
| langchain        | 0.3.26  |
| langchain-ollama | 0.3.3   |

## Running

Start the containers.
```bash
docker compose up -d
```

Before starting chat, do you need push the <b>llama3.2</b> model.
```bash
docker exec -it ollama ollama pull llama3.2
```

The Streamlit based app running on http://localhost:8000