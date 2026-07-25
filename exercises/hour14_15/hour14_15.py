"""
Hours 14-15

RAG With LangChain

✅ LLM
✅ Claude API
✅ LangChain
✅ LangGraph
✅ LangSmith
✅ Separate Agent
✅ Separate Tools
✅ Loaders
✅ Text Splitting
✅ Embeddings
✅ Vector Store
✅ Retriever
✅ Grounded Generation
✅ Browser UI
"""

import os
import streamlit as st
from dotenv import load_dotenv

# ==========================================================
# LANGSMITH
# ==========================================================

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Hours14-15-RAG"

# ==========================================================
# ENVIRONMENT
# ==========================================================

load_dotenv()

api_key = os.getenv(
    "ANTHROPIC_API_KEY"
)

# ==========================================================
# CLAUDE API + LANGCHAIN
# ==========================================================

from langchain_anthropic import (
    ChatAnthropic
)

llm = ChatAnthropic(
    model="claude-haiku-4-5-20251001",
    anthropic_api_key=api_key
)

# ==========================================================
# TOOLS
# ==========================================================

from tools.loader_tool import (
    load_documents
)

from tools.splitter_tool import (
    split_documents
)

from tools.vectorstore_tool import (
    build_vectorstore
)

from tools.retriever_tool import (
    create_retriever
)

# ==========================================================
# LOAD KB
# ==========================================================

documents = load_documents(
    "exercises/hour14_15/docs/knowledge_base.txt"
)

chunks = split_documents(
    documents
)

vectorstore = build_vectorstore(
    chunks
)

retriever = create_retriever(
    vectorstore
)

# ==========================================================
# AGENT
# ==========================================================

from agents.rag_agent import (
    RAGAgent
)

agent = RAGAgent(
    llm,
    retriever
)

# ==========================================================
# LANGGRAPH
# ==========================================================

from langgraph.graph import (
    StateGraph,
    END
)

def agent_node(state):

    result = agent.execute(
        state["question"]
    )

    state["result"] = result

    return state


workflow = StateGraph(dict)

workflow.add_node(
    "agent",
    agent_node
)

workflow.set_entry_point(
    "agent"
)

workflow.add_edge(
    "agent",
    END
)

graph = workflow.compile()

# ==========================================================
# STREAMLIT UI
# ==========================================================

st.set_page_config(
    page_title="Hours 14-15 RAG"
)

st.title(
    "📚 Hours 14-15 RAG With LangChain"
)

st.success(
    "Claude API Connected"
)

st.info(
"""
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
"""
)

question = st.text_area(
    "Ask Knowledge Base",
    "What is RAG?"
)

if st.button(
    "Ask"
):

    result = graph.invoke(
        {
            "question": question
        }
    )

    st.subheader(
        "Answer"
    )

    st.write(
        result["result"]["answer"]
    )

    st.subheader(
        "Retrieved Sources"
    )

    for doc in result["result"]["source_docs"]:

        st.code(
            doc.page_content
        )

    st.subheader(
        "Execution Flow"
    )

    st.code(
"""
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
"""
    )