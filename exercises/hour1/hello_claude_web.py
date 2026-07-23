"""
Hour 1 - Setup and Environment

Demonstrates:

✅ LLM
✅ Claude API
✅ LangChain
✅ LangGraph
✅ LangSmith
✅ Agent
✅ Tool
✅ Browser UI
"""

import os
import streamlit as st
from dotenv import load_dotenv

# ==========================================================
# LANGSMITH
# ==========================================================
# LangSmith provides tracing and observability.
#
# If LANGCHAIN_API_KEY is configured,
# traces will appear in LangSmith.
# ==========================================================

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Hour1-Claude-Demo"

# ==========================================================
# LOAD ENVIRONMENT VARIABLES
# ==========================================================

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")

# ==========================================================
# CLAUDE API
# ==========================================================
# Used to authenticate with Anthropic Claude.
# ==========================================================

# ==========================================================
# LANGCHAIN
# ==========================================================
# LangChain provides abstraction over Claude.
# ==========================================================

from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage

# ==========================================================
# LLM
# ==========================================================
# Claude Haiku model.
#
# LangChain
#    ↓
# Claude API
#    ↓
# Claude Haiku LLM
# ==========================================================

llm = ChatAnthropic(
    model="claude-haiku-4-5-20251001",
    anthropic_api_key=api_key
)

# ==========================================================
# TOOL
# ==========================================================
# Tool = capability available to Agent.
# ==========================================================

def hello_tool():

    return "Hello from Hour 1 Tool"


# ==========================================================
# AGENT NODE
# ==========================================================
# Agent decides whether Tool should be used.
# ==========================================================

def agent_node(state):

    tool_result = hello_tool()

    state["tool_result"] = tool_result

    return state


# ==========================================================
# LLM NODE
# ==========================================================
# LangChain invokes Claude API and Claude LLM.
# ==========================================================

def llm_node(state):

    response = llm.invoke(
        [
            HumanMessage(
                content=f"""
                Introduce yourself in exactly 3 lines.

                Tool Output:
                {state['tool_result']}
                """
            )
        ]
    )

    state["response"] = response.content

    return state


# ==========================================================
# LANGGRAPH
# ==========================================================
# LangGraph orchestrates workflow execution.
#
# Agent
#   ↓
# Tool
#   ↓
# LLM
# ==========================================================

from langgraph.graph import StateGraph, END

workflow = StateGraph(dict)

workflow.add_node(
    "agent",
    agent_node
)

workflow.add_node(
    "llm",
    llm_node
)

workflow.set_entry_point(
    "agent"
)

workflow.add_edge(
    "agent",
    "llm"
)

workflow.add_edge(
    "llm",
    END
)

graph = workflow.compile()

# ==========================================================
# STREAMLIT UI
# ==========================================================

st.set_page_config(
    page_title="Hour 1 Claude Demo"
)

st.title(
    "🤖 Hour 1 Claude Demo"
)

if not api_key:

    st.error(
        "Claude API Key Not Found"
    )

    st.stop()

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

✅ Agent

✅ Tool
"""
)

if st.button(
    "Call Claude"
):

    # ======================================================
    # EXECUTE LANGGRAPH WORKFLOW
    # ======================================================

    result = graph.invoke({})

    st.subheader(
        "Claude Response"
    )

    st.write(
        result["response"]
    )

    st.subheader(
        "Tool Output"
    )

    st.code(
        result["tool_result"]
    )

    st.subheader(
        "Execution Flow"
    )

    st.code(
        """
Browser
 ↓
Agent
 ↓
Tool
 ↓
LangGraph
 ↓
LangChain
 ↓
Claude API
 ↓
Claude LLM
 ↓
LangSmith Trace
 ↓
Response
        """
    )