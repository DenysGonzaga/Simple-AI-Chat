# Simple AI Chat
A simple AI chat using Ollama, Streamlit and Docker.

This app is using <a href="https://www.langchain.com/">langchain</a> to control the chain and to keep an in memory context.

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

Before starting chat, do you need pull the <b>llama3.2</b> model.
```bash
docker exec -it ollama ollama pull llama3.2
```
![pull](assets\pull_image.png?raw=true)


Or, you will get the following error:

![error](assets\error_page.png?raw=true)

The Streamlit based app running on http://localhost:8000

![pull](assets\chating.png?raw=true)

Happy Chat ! 