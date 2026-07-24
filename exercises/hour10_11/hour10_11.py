"""
Hours 10-11

Context Engineering and Memory Basics

Concepts Covered
✅ Context Selection
✅ Conversation Summarization
✅ Short-Term Memory
✅ Long-Term Memory

Technologies Demonstrated
✅ LLM
✅ Claude API
✅ LangChain
✅ LangGraph
✅ LangSmith
✅ Agent
✅ Tools
✅ Memory
✅ Browser UI
"""

import os
import json
import streamlit as st
from dotenv import load_dotenv
from typing import TypedDict

# ==========================================================
# LANGSMITH
# ==========================================================
# LangSmith = Observability & Tracing
# Tracks LangChain + LangGraph executions
# ==========================================================

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Hours10-11-MemoryChatbot"

# ==========================================================
# ENVIRONMENT
# ==========================================================

load_dotenv()

# ==========================================================
# CLAUDE API
# ==========================================================
# Claude API Key from .env
# ==========================================================

api_key = os.getenv("ANTHROPIC_API_KEY")

if not api_key:
    raise ValueError(
        "ANTHROPIC_API_KEY not found"
    )

# ==========================================================
# LANGCHAIN
# ==========================================================
# LangChain = abstraction layer
# between application and LLM
# ==========================================================

from langchain_anthropic import ChatAnthropic

# ==========================================================
# LLM
# ==========================================================
# Claude Haiku model
# ==========================================================

llm = ChatAnthropic(
    model="claude-haiku-4-5-20251001",
    anthropic_api_key=api_key
)

# ==========================================================
# SHORT TERM MEMORY
# ==========================================================
# Short-term memory lives only
# during the browser session
# ==========================================================

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "session_summary" not in st.session_state:
    st.session_state.session_summary = ""

# ==========================================================
# LONG TERM MEMORY
# ==========================================================
# Stores remembered facts
# ==========================================================

if "memory_store" not in st.session_state:
    st.session_state.memory_store = {}

# ==========================================================
# TOOL 1
# MEMORY STORAGE TOOL
# ==========================================================
# Stores user facts/preferences
# ==========================================================

def memory_store_tool(user_input):

    text = user_input.lower()

    # ==========================================
    # Store Name
    # ==========================================

    if "my name is" in text:

        name = user_input.split("is")[-1].strip()

        st.session_state.memory_store["name"] = name

        return f"Stored Name: {name}"

    # ==========================================
    # Store Role
    # Supports:
    # I am a Technical Lead
    # I am Technical Lead
    # i am a technical lead
    # ==========================================

    if "i am" in text:

        role = user_input.lower()

        role = role.replace(
            "i am a",
            ""
        )

        role = role.replace(
            "i am",
            ""
        )

        role = role.strip().title()

        st.session_state.memory_store["role"] = role

        return f"Stored Role: {role}"

    # ==========================================
    # Store Favorite Color
    # ==========================================

    if "my favorite color is" in text:

        color = user_input.split("is")[-1].strip()

        st.session_state.memory_store["favorite_color"] = color

        return f"Stored Favorite Color: {color}"

    return "No memory extracted"

# ==========================================================
# TOOL 2
# MEMORY RECALL TOOL
# ==========================================================
# Retrieves stored memory
# ==========================================================

def memory_recall_tool():

    if not st.session_state.memory_store:

        return "No memory stored yet."

    result = []

    for key, value in st.session_state.memory_store.items():

        result.append(
            f"{key}: {value}"
        )

    return "\n".join(result)

# ==========================================================
# TOOL 3
# SUMMARY TOOL
# ==========================================================
# Builds session summary
# ==========================================================

def summary_tool():

    if not st.session_state.chat_history:

        return "No conversation history."

    summary_prompt = f"""
    Summarize this conversation:

    {json.dumps(st.session_state.chat_history)}
    """

    return llm.invoke(
        summary_prompt
    ).content

# ==========================================================
# AGENT
# ==========================================================
# Agent decides which tool to call
# ==========================================================

def agent_router(user_input):

    text = user_input.lower()

    if (
        "my name is" in text
        or "i am a" in text
        or "favorite color" in text
    ):
        return "memory_store"

    if "what do you know about me" in text:
        return "memory_recall"

    if "show session summary" in text:
        return "summary"

    return "chat"

# ==========================================================
# LANGGRAPH
# ==========================================================
# LangGraph workflow:
#
# User
#  ↓
# Agent
#  ↓
# Tool
#  ↓
# LLM
# ==========================================================

from langgraph.graph import (
    StateGraph,
    END
)

class GraphState(TypedDict):

    # User message
    user_input: str

    # Agent decision
    route: str

    # Final response
    response: str

# ==========================================================
# AGENT NODE
# ==========================================================

def agent_node(state):

    user_input = state["user_input"]

    route = agent_router(
        user_input
    )

    state["route"] = route

    return state

# ==========================================================
# TOOL NODE
# ==========================================================

def tool_node(state):

    route = state.get(
    "route",
    "chat"
    )

    user_input = state["user_input"]

    if route == "memory_store":

        state["response"] = (
            memory_store_tool(
                user_input
            )
        )

    elif route == "memory_recall":

        state["response"] = (
            memory_recall_tool()
        )

    elif route == "summary":

        state["response"] = (
            summary_tool()
        )

    return state

# ==========================================================
# LLM NODE
# ==========================================================
# Context Engineering
#
# Uses:
# 1. Memory
# 2. Session Summary
# 3. Current Message
# ==========================================================

def llm_node(state):

    if state["route"] != "chat":

        return state

    memory_context = json.dumps(
        st.session_state.memory_store,
        indent=2
    )

    prompt = f"""
    Context Memory:
    {memory_context}

    Session Summary:
    {st.session_state.session_summary}

    User:
    {state['user_input']}

    Answer using the context.
    """

    response = llm.invoke(
        prompt
    ).content

    state["response"] = response

    return state

# ==========================================================
# GRAPH BUILD
# ==========================================================

workflow = StateGraph(GraphState)

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
    page_title="Hours 10-11 Memory Chatbot"
)

st.title(
    "🧠 Hours 10-11 Memory Chatbot"
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
✅ Context Engineering
✅ Short-Term Memory
✅ Long-Term Memory
✅ Session Summary
"""
)

user_input = st.text_input(
    "Ask Something"
)

if st.button("Send"):

    result = graph.invoke(
        {
            "user_input": user_input
        }
    )

    response = result["response"]

    st.session_state.chat_history.append(
        {
            "user": user_input,
            "bot": response
        }
    )

    st.session_state.session_summary += (
        f"\nUser: {user_input}"
    )

    st.subheader("Response")

    st.write(response)

# ==========================================================
# MEMORY DISPLAY
# ==========================================================

st.subheader(
    "Stored Long-Term Memory"
)

st.json(
    st.session_state.memory_store
)

# ==========================================================
# SESSION SUMMARY
# ==========================================================

st.subheader(
    "Short-Term Memory / Session Summary"
)

st.text_area(
    "",
    st.session_state.session_summary,
    height=200
)

# ==========================================================
# CHAT HISTORY
# ==========================================================

st.subheader(
    "Chat History"
)

for item in st.session_state.chat_history:

    st.write(
        f"👤 {item['user']}"
    )

    st.write(
        f"🤖 {item['bot']}"
    )