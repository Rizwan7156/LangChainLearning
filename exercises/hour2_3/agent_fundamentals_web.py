"""
Hours 2-3 - Agentic Framework Fundamentals

Technologies Demonstrated

✅ LLM
✅ Claude API
✅ LangChain
✅ LangGraph
✅ LangSmith
✅ Agent
✅ Tools
✅ State
✅ Guardrails
✅ Harness
✅ Streamlit Browser UI
"""

import os
import streamlit as st
from dotenv import load_dotenv
from datetime import date

# ==========================================================
# LANGSMITH
# ==========================================================
# LangSmith is used for tracing and observability.
#
# If LANGCHAIN_API_KEY is configured,
# execution traces will be visible in LangSmith.
# ==========================================================

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Hour2-3-Agent-Fundamentals"

# ==========================================================
# LOAD ENVIRONMENT
# ==========================================================

load_dotenv()

# ==========================================================
# CLAUDE API
# ==========================================================
# Authenticate with Anthropic Claude
# ==========================================================

api_key = os.getenv("ANTHROPIC_API_KEY")

# ==========================================================
# GUARDRAIL
# ==========================================================
# Prevent execution if API Key is missing.
# ==========================================================

if not api_key:
    raise ValueError(
        "ANTHROPIC_API_KEY not found in .env"
    )

# ==========================================================
# LANGCHAIN
# ==========================================================
# LangChain provides abstraction over Claude.
# ==========================================================

from langchain_anthropic import ChatAnthropic

# ==========================================================
# LLM
# ==========================================================
# Claude Haiku is the actual LLM.
#
# LangChain
#      ↓
# Claude API
#      ↓
# Claude Haiku
# ==========================================================

llm = ChatAnthropic(
    model="claude-haiku-4-5-20251001",
    anthropic_api_key=api_key
)

# ==========================================================
# TOOL 1
# ==========================================================
# Tool available to Agent.
#
# Returns today's date.
# ==========================================================

def get_date_tool():

    return str(date.today())


# ==========================================================
# TOOL 2
# ==========================================================
# Calculator Tool
#
# Allows Agent to perform calculations.
# ==========================================================

def calculator_tool(expression):

    try:
        return str(eval(expression))
    except Exception:
        return "Invalid calculation"


# ==========================================================
# STATE
# ==========================================================
# Shared state used by LangGraph.
#
# State moves across:
#
# Agent
#     ↓
# Tool
#     ↓
# LLM
# ==========================================================

# ==========================================================
# AGENT NODE
# ==========================================================
# Agent decides:
#
# Which Tool to execute.
#
# Examples:
#
# date question
#    ↓
# Date Tool
#
# 25 * 10
#    ↓
# Calculator Tool
#
# General AI question
#    ↓
# No Tool
# ==========================================================

def agent_node(state):

    prompt = state["prompt"]

    if "date" in prompt.lower():

        state["selected_tool"] = "date"

    elif any(
        op in prompt
        for op in ["+", "-", "*", "/"]
    ):

        state["selected_tool"] = "calculator"

    else:

        state["selected_tool"] = "none"

    return state


# ==========================================================
# TOOL NODE
# ==========================================================
# Executes Tool selected by Agent.
# ==========================================================

def tool_node(state):

    selected_tool = state["selected_tool"]

    if selected_tool == "date":

        state["tool_result"] = (
            get_date_tool()
        )

    elif selected_tool == "calculator":

        state["tool_result"] = (
            calculator_tool(
                state["prompt"]
            )
        )

    else:

        state["tool_result"] = (
            "No Tool Required"
        )

    return state


# ==========================================================
# LLM NODE
# ==========================================================
# LangChain invokes Claude.
#
# LangChain
#      ↓
# Claude API
#      ↓
# Claude LLM
# ==========================================================

def llm_node(state):

    response = llm.invoke(
        f"""
        User Prompt:
        {state['prompt']}

        Selected Tool:
        {state['selected_tool']}

        Tool Result:
        {state['tool_result']}

        Explain the answer clearly.
        """
    )

    state["response"] = response.content

    return state


# ==========================================================
# LANGGRAPH
# ==========================================================
# LangGraph executes workflow.
#
# Agent Node
#      ↓
# Tool Node
#      ↓
# LLM Node
# ==========================================================

from langgraph.graph import (
    StateGraph,
    END
)

workflow = StateGraph(dict)

workflow.add_node(
    "agent",
    agent_node
)

workflow.add_node(
    "tool",
    tool_node
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
    "tool"
)

workflow.add_edge(
    "tool",
    "llm"
)

workflow.add_edge(
    "llm",
    END
)

graph = workflow.compile()

# ==========================================================
# HARNESS
# ==========================================================
# Harness orchestrates:
#
# Prompt
# State
# Agent
# Tool
# LLM
# Response
#
# Entire application acts as the Harness.
# ==========================================================

# ==========================================================
# STREAMLIT BROWSER UI
# ==========================================================

st.set_page_config(
    page_title="Hours 2-3 Agent Fundamentals"
)

st.title(
    "🤖 Hours 2-3 Agentic Framework Fundamentals"
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

✅ Agent

✅ Tools

✅ State

✅ Guardrails

✅ Harness
"""
)

prompt = st.text_area(
    "Enter Prompt",
    "What is today's date?"
)

# ==========================================================
# GUARDRAIL
# ==========================================================
# Empty prompts are not allowed.
# ==========================================================

if st.button("Run Agent"):

    if not prompt.strip():

        st.warning(
            "Please enter a prompt."
        )

        st.stop()

    # ======================================================
    # Execute LangGraph Workflow
    # ======================================================

    result = graph.invoke(
        {
            "prompt": prompt
        }
    )

    st.subheader(
        "Agent Response"
    )

    st.write(
        result["response"]
    )

    st.subheader(
        "Agent Decisions"
    )

    st.code(
        f"""
Selected Tool:
{result['selected_tool']}

Tool Result:
{result['tool_result']}
        """
    )

    st.subheader(
        "Execution Flow"
    )

    st.code(
        """
Browser
 ↓
Prompt
 ↓
Harness
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