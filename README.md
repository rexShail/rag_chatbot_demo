# RAG Agent Localhost

Run the PDF document loader with:

```sh
uv run rag-agent-localhost
```

The loader reads PDF files from `src/rag_agent_localhost/data` and creates one
LangChain document for each page with extractable text.