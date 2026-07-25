"""
Hours 19-20

Tracing, Evaluation and Capstone Integration

✅ LLM
✅ Claude API
✅ LangChain
✅ LangGraph
✅ LangSmith

✅ Supervisor Agent
✅ Chat Agent
✅ RAG Agent
✅ Evaluation Agent
✅ Human Review Agent

✅ Tools

✅ Tracing
✅ Evaluation
✅ Human Approval
✅ Dataset Evaluation

✅ Browser UI
"""

import os
import streamlit as st
from dotenv import load_dotenv

# ==========================================================
# LANGSMITH
# ==========================================================

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Hours19-20-Capstone"

# ==========================================================
# ENVIRONMENT
# ==========================================================

load_dotenv()

# ==========================================================
# LLM + CLAUDE API
# ==========================================================

from langchain_anthropic import ChatAnthropic

llm = ChatAnthropic(
    model="claude-haiku-4-5-20251001",
    anthropic_api_key=os.getenv(
        "ANTHROPIC_API_KEY"
    )
)

# ==========================================================
# AGENTS
# ==========================================================

from agents.supervisor_agent import SupervisorAgent
from agents.chat_agent import ChatAgent
from agents.rag_agent import RagAgent
from agents.evaluation_agent import EvaluationAgent
from agents.human_review_agent import HumanReviewAgent

supervisor = SupervisorAgent()
chat_agent = ChatAgent(llm)
evaluation_agent = EvaluationAgent()
review_agent = HumanReviewAgent()

# ==========================================================
# SIMPLE RAG KNOWLEDGE BASE
# ==========================================================

from langchain_core.documents import Document
from langchain_community.embeddings import FakeEmbeddings
from langchain_community.vectorstores import FAISS

docs = [

    Document(
        page_content=
        "LangGraph is a workflow orchestration framework."
    ),

    Document(
        page_content=
        "LangChain helps build LLM applications."
    ),

    Document(
        page_content=
        "RAG stands for Retrieval Augmented Generation."
    )

]

embeddings = FakeEmbeddings(
    size=768
)

vectorstore = FAISS.from_documents(
    docs,
    embeddings
)

retriever = vectorstore.as_retriever()

rag_agent = RagAgent(
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

# ==========================================================
# ROUTE NODE
# ==========================================================

def route_node(state):

    state["route"] = supervisor.route(
        state["question"]
    )

    return state


# ==========================================================
# CHAT NODE
# ==========================================================

def chat_node(state):

    answer = chat_agent.execute(
        state["question"]
    )

    state["answer"] = answer

    return state


# ==========================================================
# RAG NODE
# ==========================================================

def rag_node(state):

    answer = rag_agent.execute(
        state["question"]
    )

    state["answer"] = answer

    return state


# ==========================================================
# EVALUATION NODE
# ==========================================================

def evaluation_node(state):

    result = evaluation_agent.run()

    state["answer"] = result

    return state


# ==========================================================
# REVIEW NODE
# Human review happens OUTSIDE graph
# ==========================================================

def review_node(state):

    return state


# ==========================================================
# ROUTING FUNCTION
# ==========================================================

def route_function(state):

    return state["route"]


# ==========================================================
# BUILD GRAPH
# ==========================================================

workflow = StateGraph(dict)

workflow.add_node(
    "route",
    route_node
)

workflow.add_node(
    "chat",
    chat_node
)

workflow.add_node(
    "rag",
    rag_node
)

workflow.add_node(
    "evaluation",
    evaluation_node
)

workflow.add_node(
    "review",
    review_node
)

workflow.set_entry_point(
    "route"
)

workflow.add_conditional_edges(
    "route",
    route_function,
    {
        "chat": "chat",
        "rag": "rag",
        "evaluation": "evaluation"
    }
)

workflow.add_edge(
    "chat",
    "review"
)

workflow.add_edge(
    "rag",
    "review"
)

workflow.add_edge(
    "evaluation",
    "review"
)

workflow.add_edge(
    "review",
    END
)

graph = workflow.compile()

# ==========================================================
# UI
# ==========================================================

st.set_page_config(
    page_title="Hours 19-20 Capstone"
)

st.title(
    "✅ Hours 19-20 Capstone Integration"
)

question = st.text_area(
    "Question",
    "Run Evaluation"
)

# ==========================================================
# EXECUTE WORKFLOW
# ==========================================================

if st.button(
    "Execute"
):

    st.session_state["workflow_result"] = graph.invoke(
        {
            "question": question
        }
    )

# ==========================================================
# HUMAN REVIEW CHECKPOINT
# ==========================================================

if "workflow_result" in st.session_state:

    st.subheader(
        "Human Review Checkpoint"
    )

    approval_choice = st.radio(
        "Review Decision",
        [
            "Approve",
            "Reject"
        ]
    )

    approved = (
        approval_choice == "Approve"
    )

    final_result = review_agent.review(
        st.session_state[
            "workflow_result"
        ]["answer"],
        approved
    )

    st.subheader(
        "Final Result"
    )

    st.json(
        final_result
    )
# ==========================================================
# SHOW SELECTED ROUTE
# ==========================================================

if (
    "workflow_result" in st.session_state
    and "route" in st.session_state["workflow_result"]
):

    st.subheader(
        "Selected Route"
    )

    st.code(
        st.session_state[
            "workflow_result"
        ]["route"]
    )
# ==========================================================
# WORKFLOW DISPLAY
# ==========================================================

st.subheader(
    "Workflow"
)

st.code(
"""
User
 ↓

Supervisor Agent

 ├── Chat Agent
 ├── RAG Agent
 └── Evaluation Agent

 ↓

Human Review Agent

 ↓

Approval Tool

 ↓

LangSmith Trace

 ↓

Final Response
"""
)