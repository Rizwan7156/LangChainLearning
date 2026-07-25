"""
Hours 16-18

LangGraph Workflows Expanded

Technologies Demonstrated

✅ LLM
✅ Claude API
✅ LangChain
✅ LangGraph
✅ LangSmith

✅ Supervisor Agent
✅ Chat Agent
✅ RAG Agent

✅ Tools
✅ Routing Tool
✅ Checkpointer
✅ Memory Tool

✅ StateGraph
✅ Nodes
✅ Edges
✅ Branching
✅ Resume Behaviour

✅ Browser UI
"""

import os
import streamlit as st
from dotenv import load_dotenv

# ==========================================================
# LANGSMITH
# ==========================================================

os.environ[
    "LANGCHAIN_TRACING_V2"
] = "true"

os.environ[
    "LANGCHAIN_PROJECT"
] = "Hours16-18-LangGraph"

# ==========================================================
# ENVIRONMENT
# ==========================================================

load_dotenv()

api_key = os.getenv(
    "ANTHROPIC_API_KEY"
)

# ==========================================================
# LANGCHAIN
# ==========================================================

from langchain_anthropic import (
    ChatAnthropic
)

# ==========================================================
# LLM
# ==========================================================

llm = ChatAnthropic(
    model="claude-haiku-4-5-20251001",
    anthropic_api_key=api_key
)

# ==========================================================
# KNOWLEDGE BASE
# ==========================================================

from langchain_core.documents import (
    Document
)

docs = [

    Document(
        page_content=
        "RAG stands for Retrieval Augmented Generation."
    ),

    Document(
        page_content=
        "LangGraph is a workflow orchestration framework."
    ),

    Document(
        page_content=
        "LangChain helps build LLM applications."
    )
]

# ==========================================================
# VECTOR STORE
# ==========================================================

from langchain_community.embeddings import (
    FakeEmbeddings
)

from langchain_community.vectorstores import (
    FAISS
)

embeddings = FakeEmbeddings(
    size=768
)

vectorstore = FAISS.from_documents(
    docs,
    embeddings
)

retriever = (
    vectorstore.as_retriever()
)

# ==========================================================
# AGENTS
# ==========================================================

from agents.supervisor_agent import (
    SupervisorAgent
)

from agents.chat_agent import (
    ChatAgent
)

from agents.rag_agent import (
    RagAgent
)

supervisor = (
    SupervisorAgent()
)

chat_agent = (
    ChatAgent(llm)
)

rag_agent = (
    RagAgent(
        llm,
        retriever
    )
)

# ==========================================================
# TOOLS
# ==========================================================

from tools.checkpoint_tool import (
    get_memory_checkpointer
)

checkpointer = (
    get_memory_checkpointer()
)

# ==========================================================
# LANGGRAPH
# ==========================================================

from langgraph.graph import (
    StateGraph,
    END
)

# Agent Node

def supervisor_node(state):

    route = supervisor.route(
        state["question"]
    )

    state["route"] = route

    return state


# Chat Node

def chat_node(state):

    state["response"] = (
        chat_agent.execute(
            state["question"]
        )
    )

    return state


# RAG Node

def rag_node(state):

    state["response"] = (
        rag_agent.execute(
            state["question"]
        )
    )

    return state


# Routing Function

def route_function(state):

    return state["route"]


workflow = StateGraph(dict)

workflow.add_node(
    "supervisor",
    supervisor_node
)

workflow.add_node(
    "chat",
    chat_node
)

workflow.add_node(
    "rag",
    rag_node
)

workflow.set_entry_point(
    "supervisor"
)

workflow.add_conditional_edges(
    "supervisor",
    route_function,
    {
        "chat": "chat",
        "rag": "rag"
    }
)

workflow.add_edge(
    "chat",
    END
)

workflow.add_edge(
    "rag",
    END
)

graph = workflow.compile(
    checkpointer=checkpointer
)

# ==========================================================
# UI
# ==========================================================

st.set_page_config(
    page_title="Hours 16-18"
)

st.title(
    "🔀 Hours 16-18 LangGraph Workflows"
)

st.success(
    "Claude API Connected"
)

question = st.text_area(
    "Ask Question",
    "What is LangGraph?"
)

if st.button(
    "Execute Workflow"
):

    result = graph.invoke(
        {
            "question": question
        },
        config={
            "configurable": {
                "thread_id": "demo_user"
            }
        }
    )

    st.subheader(
        "Response"
    )

    st.write(
        result["response"]
    )

    st.subheader(
        "Selected Route"
    )

    st.code(
        result["route"]
    )

    st.subheader(
        "Workflow"
    )

    st.code(
"""
User
 ↓
Supervisor Agent
 ↓

Branch

 ├── Chat Agent
 │
 └── RAG Agent

 ↓

Checkpointer

 ↓

Response
"""
    )