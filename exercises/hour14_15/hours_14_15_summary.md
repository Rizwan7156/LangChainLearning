# Hours 14-15 Summary

## Topic

RAG With LangChain

---

## Concepts Covered

- Loaders
- Text Splitting
- Embeddings
- Vector Store
- Retriever
- Grounded Generation
- RAG Pipeline

---

## Technologies Demonstrated

✅ LLM

✅ Claude API

✅ LangChain

✅ LangGraph

✅ LangSmith

✅ Separate Agent

✅ Separate Tools

✅ Loader

✅ Splitter

✅ Embeddings

✅ Vector Store

✅ Retriever

✅ Grounded Generation

✅ Browser UI

---

## Architecture

Browser
↓
RAG Agent
↓
Retriever
↓
Vector Store
↓
Relevant Chunks
↓
Claude
↓
Grounded Answer

---

## Files Created

- agents/rag_agent.py
- tools/loader_tool.py
- tools/splitter_tool.py
- tools/vectorstore_tool.py
- tools/retriever_tool.py
- docs/knowledge_base.txt
- hour14_15.py

---

## Deliverable

A complete Retrieval Augmented Generation (RAG) solution that:

- Loads documents
- Splits content into chunks
- Creates embeddings
- Builds a vector store
- Retrieves relevant context
- Generates grounded answers
- Displays cited snippets

---

## Reviewer Talking Point

Hours 12-13 introduced a separate Agent.

Hours 14-15 extends that architecture by introducing:

- Separate Agent
- Separate Tools
- Retrieval Pipeline
- Retrieval-Augmented Generation (RAG)
- Grounded Answers from Documents