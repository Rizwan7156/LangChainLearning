"""
Hours 6-7

Tools and Tool Calling

Technologies Demonstrated

✅ LLM
✅ Claude API
✅ LangChain
✅ LangGraph
✅ LangSmith
✅ Agent
✅ Tools
✅ Tool Validation
✅ Error Handling
✅ Browser UI
"""

import os
import streamlit as st
from dotenv import load_dotenv
from datetime import date

# ==========================================================
# LANGSMITH
# ==========================================================
# Tracing and observability
# ==========================================================

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Hours6-7-Tools"

# ==========================================================
# LOAD ENVIRONMENT
# ==========================================================

load_dotenv()

# ==========================================================
# CLAUDE API
# ==========================================================

api_key = os.getenv("ANTHROPIC_API_KEY")

if not api_key:
    raise ValueError(
        "ANTHROPIC_API_KEY not found"
    )

# ==========================================================
# LANGCHAIN
# ==========================================================

from langchain_anthropic import ChatAnthropic

# ==========================================================
# LLM
# ==========================================================

llm = ChatAnthropic(
    model="claude-haiku-4-5-20251001",
    anthropic_api_key=api_key
)

# ==========================================================
# TOOL SCHEMA
# ==========================================================
# Tools available for Agent
# ==========================================================

def date_tool():

    return str(date.today())

# ==========================================================
# TOOL
# Calculator
# ==========================================================

def calculator_tool(expression):

    try:

        result = eval(expression)

        return str(result)

    except Exception:

        return "Calculation Error"

# ==========================================================
# TOOL
# Mock Order Status
# ==========================================================

def order_status_tool(order_id):

    mock_db = {
        "1001": "Shipped",
        "1002": "Processing",
        "1003": "Delivered"
    }

    return mock_db.get(
        order_id,
        "Order Not Found"
    )

# ==========================================================
# AGENT
# Tool Selection Logic
# ==========================================================

def agent_node(state):

    prompt = state["prompt"]

    if "date" in prompt.lower():

        state["tool"] = "date"

    elif "order" in prompt.lower():

        state["tool"] = "order"

    elif any(
        op in prompt
        for op in ["+", "-", "*", "/"]
    ):

        state["tool"] = "calculator"

    else:

        state["tool"] = "none"

    return state

# ==========================================================
# TOOL VALIDATION
# ==========================================================

def validate_tool_node(state):

    allowed_tools = [
        "date",
        "order",
        "calculator",
        "none"
    ]

    if state["tool"] not in allowed_tools:

        state["tool"] = "none"

    return state

# ==========================================================
# TOOL EXECUTION
# ==========================================================

def tool_node(state):

    prompt = state["prompt"]

    tool_name = state["tool"]

    if tool_name == "date":

        state["tool_result"] = (
            date_tool()
        )

    elif tool_name == "calculator":

        state["tool_result"] = (
            calculator_tool(prompt)
        )

    elif tool_name == "order":

        order_id = "".join(
            c for c in prompt
            if c.isdigit()
        )

        state["tool_result"] = (
            order_status_tool(order_id)
        )

    else:

        state["tool_result"] = (
            "No Tool Required"
        )

    return state

# ==========================================================
# LLM NODE
# ==========================================================
# LangChain
# ↓
# Claude API
# ↓
# Claude LLM
# ==========================================================

def llm_node(state):

    response = llm.invoke(
        f"""
        User Prompt:
        {state['prompt']}

        Selected Tool:
        {state['tool']}

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
# Agent
# ↓
# Validation
# ↓
# Tool
# ↓
# LLM
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
    "validation",
    validate_tool_node
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
    "validation"
)

workflow.add_edge(
    "validation",
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
# STREAMLIT UI
# ==========================================================

st.set_page_config(
    page_title="Hours 6-7 Tool Calling Agent"
)

st.title(
    "🛠️ Hours 6-7 Tool Calling Agent"
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

✅ Tool Validation

✅ Error Handling
"""
)

prompt = st.text_input(
    "Enter Prompt",
    "What is today's date?"
)

if st.button(
    "Run Agent"
):

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
        "Tool Details"
    )

    st.code(
        f"""
Selected Tool:
{result['tool']}

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
Agent
 ↓
Tool Validation
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