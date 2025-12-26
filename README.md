# AI Agent with Rag

Simple RAG demo for restaurant reviews (LangChain + Chroma + Ollama).

## Before running
You must pull the Ollama models you plan to use BEFORE running the app:

```bash
ollama pull llama3.2      # LLM
ollama pull phi3         # light LLM
# choose one of the above LLMs
ollama pull mxbai-embed-large  # for embedding
```

Ensure the Ollama service/daemon is running and the chosen models are available locally.

## Install
Install Python dependencies from the provided `requirements.txt` (use your preferred venv):

```bash
pip install -r requirements.txt
```

## Run
Start the app:

```bash
python main.py
```

When prompted, enter questions (or `q` to quit).

## Notes
- The repo expects the dataset `realistic_restaurant_reviews.csv` in the project root.
- If the Ollama embedding/model is unavailable, the code contains safe fallbacks to avoid crashes; results may be limited.
