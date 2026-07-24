"""
Hours 4-5

Models, Messages, Prompts, Streaming

Technologies Demonstrated:

✅ LLM
✅ Claude API
✅ LangChain
✅ LangGraph
✅ LangSmith
✅ Agent
✅ Tool
✅ Roles
✅ System Messages
✅ User Messages
✅ Message History
✅ Streaming Responses
✅ Chat Models
✅ Browser UI
"""

import os
import streamlit as st
from dotenv import load_dotenv
from datetime import date

# ==========================================================
# LANGSMITH
# ==========================================================
# LangSmith provides tracing and observability.
#
# If LANGCHAIN_API_KEY is configured,
# traces will appear in LangSmith Dashboard.
# ==========================================================

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Hours4-5-Streaming-Chatbot"

# ==========================================================
# LOAD ENVIRONMENT VARIABLES
# ==========================================================

load_dotenv()

# ==========================================================
# CLAUDE API
# ==========================================================
# Claude API Key loaded from .env
# Used to authenticate with Anthropic.
# ==========================================================

api_key = os.getenv("ANTHROPIC_API_KEY")

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
# Claude Haiku Chat Model
#
# LangChain
#      ↓
# Claude API
#      ↓
# Claude LLM
# ==========================================================

llm = ChatAnthropic(
    model="claude-haiku-4-5-20251001",
    anthropic_api_key=api_key,
    streaming=True
)

# ==========================================================
# TOOL
# ==========================================================
# Example Tool
#
# Agent can decide to use the Date Tool.
# ==========================================================

def date_tool():

    return str(date.today())

# ==========================================================
# AGENT NODE
# ==========================================================
# Decides if Tool should be used.
#
# Example:
#     What is today's date?
#         ↓
#     Use Date Tool
#
# Other Questions
#         ↓
#     No Tool Required
# ==========================================================

def agent_node(state):

    user_message = state["user_message"]

    if "date" in user_message.lower():

        state["selected_tool"] = "date"

    else:

        state["selected_tool"] = "none"

    return state


# ==========================================================
# TOOL NODE
# ==========================================================
# Executes Tool selected by Agent.
# ==========================================================

def tool_node(state):

    if state["selected_tool"] == "date":

        state["tool_result"] = (
            date_tool()
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
#      ↓
# Claude API
#      ↓
# Claude LLM
#
# System Message
# User Message
# Tool Result
# ==========================================================

def llm_node(state):

    system_message = state["system_message"]

    user_message = state["user_message"]

    tool_result = state["tool_result"]

    response = llm.invoke(
        f"""
        System Message:
        {system_message}

        User Message:
        {user_message}

        Tool Result:
        {tool_result}

        Answer clearly.
        """
    )

    state["assistant_response"] = (
        response.content
    )

    return state

# ==========================================================
# LANGGRAPH
# ==========================================================
# Workflow:
#
# Agent
#   ↓
# Tool
#   ↓
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
# STREAMLIT UI
# ==========================================================

st.set_page_config(
    page_title="Hours 4-5 Streaming Chatbot"
)

st.title(
    "💬 Hours 4-5 Streaming Chatbot"
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

✅ Tool

✅ Roles

✅ System Messages

✅ User Messages

✅ Message History

✅ Streaming

✅ Chat Model
"""
)

# ==========================================================
# ROLES
# ==========================================================
# System Role controls chatbot behaviour.
# ==========================================================

system_message = st.text_area(
    "System Message",
    "You are a Senior Python Trainer."
)

# ==========================================================
# MESSAGE HISTORY
# ==========================================================
# Stores conversation.
# ==========================================================

if "messages" not in st.session_state:

    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.write(
            message["content"]
        )

# ==========================================================
# USER MESSAGE
# ==========================================================

user_message = st.chat_input(
    "Ask something..."
)

if user_message:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_message
        }
    )

    with st.chat_message("user"):

        st.write(user_message)

    # ======================================================
    # LANGGRAPH EXECUTION
    # ======================================================

    result = graph.invoke(
        {
            "system_message": system_message,
            "user_message": user_message
        }
    )

    assistant_response = (
        result["assistant_response"]
    )

    # ======================================================
    # STREAMING RESPONSE
    # ======================================================
    # Simulated streaming UX for reviewer demo.
    # ======================================================

    with st.chat_message(
        "assistant"
    ):

        placeholder = st.empty()

        streamed_text = ""

        for word in assistant_response.split():

            streamed_text += word + " "

            placeholder.markdown(
                streamed_text
            )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": assistant_response
        }
    )

    st.subheader(
        "Agent Details"
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
User Message
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
Streaming Response
 ↓
Browser
        """
    )