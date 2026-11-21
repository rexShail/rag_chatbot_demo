# rag_chatbot_demo

A Retrieval-Augmented Generation (RAG) chatbot demonstration built in Python and managed with `uv`.

## Overview

`rag_chatbot_demo` provides a modular foundation for document ingestion, vectorstore persistence, document retrieval, and conversational response generation using Retrieval-Augmented Generation.

## Project Structure

```text
rag_chatbot_demo/
├── src/               # Application source code (vectorstore persistence, retrieval, entrypoint)
├── pyproject.toml     # Project metadata and dependency definitions
├── uv.lock            # Locked dependency versions for reproducible environments
├── .gitignore         # Git ignore rules
└── LICENSE            # MIT License