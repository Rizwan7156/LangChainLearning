"""
Hours 8-9

Harness Design and Middleware

Technologies Demonstrated

✅ LLM
✅ Claude API
✅ LangChain
✅ LangGraph
✅ LangSmith
✅ Agent
✅ Tools
✅ Middleware
✅ Retry Logic
✅ Logging
✅ Guardrails
✅ Error Handling
✅ Browser UI
"""

import os
import time
import logging
import streamlit as st
from dotenv import load_dotenv
from datetime import date

# ==========================================================
# LANGSMITH
# ==========================================================

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Hours8-9-Harness"

# ==========================================================
# LOAD ENVIRONMENT
# ==========================================================

load_dotenv()

# ==========================================================
# LOGGING
# ==========================================================

logging.basicConfig(
    level=logging.INFO
)

logger = logging.getLogger(
    "Hours8_9"
)

# ==========================================================
# CLAUDE API
# ==========================================================

api_key = os.getenv(
    "ANTHROPIC_API_KEY"
)

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
# TOOL 1
# ==========================================================

def date_tool():

    return str(date.today())

# ==========================================================
# TOOL 2
# ==========================================================

def calculator_tool(expression):

    try:
        return str(eval(expression))
    except Exception:
        return "Calculation Error"

# ==========================================================
# TOOL 3
# ==========================================================

def order_tool(order_id):

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
# GUARDRAIL
# ==========================================================
# Input Validation
# ==========================================================

def validate_input(prompt):

    if not prompt.strip():

        raise ValueError(
            "Guardrail Triggered: Prompt cannot be empty"
        )

# ==========================================================
# MIDDLEWARE
# ==========================================================
# Policy Check Layer
# ==========================================================

def policy_check(prompt):

    blocked_words = [
        "hack",
        "malware"
    ]

    if any(
        word in prompt.lower()
        for word in blocked_words
    ):

        raise ValueError(
            "Middleware Policy Check Failed: Policy violation detected"
        )

# ==========================================================
# AGENT
# ==========================================================

def agent_node(state):

    prompt = state["prompt"]

    if "date" in prompt.lower():

        state["tool"] = "date"

    elif "order" in prompt.lower():

        state["tool"] = "order"

    elif any(
        op in prompt
        for op in ["+","-","*","/"]
    ):

        state["tool"] = "calculator"

    else:

        state["tool"] = "none"

    return state

# ==========================================================
# TOOL EXECUTION
# ==========================================================

def tool_node(state):

    prompt = state["prompt"]

    if state["tool"] == "date":

        state["tool_result"] = (
            date_tool()
        )

    elif state["tool"] == "calculator":

        state["tool_result"] = (
            calculator_tool(prompt)
        )

    elif state["tool"] == "order":

        order_id = "".join(
            c for c in prompt
            if c.isdigit()
        )

        state["tool_result"] = (
            order_tool(order_id)
        )

    else:

        state["tool_result"] = (
            "No Tool Required"
        )

    return state

# ==========================================================
# RETRY WRAPPER + LOGGING
# ==========================================================
# Demonstrates:
#
# ✅ Retry Logic
# ✅ Logging
# ✅ Exception Handling
#
# Visible in Browser
# ==========================================================

def call_llm_with_retry(
    prompt,
    retries=3
):

    retry_log = []

    attempt = 0

    while attempt < retries:

        try:

            log_message = (
                f"Attempt {attempt + 1} started"
            )

            retry_log.append(
                log_message
            )

            logger.info(
                log_message
            )

            # ==================================================
            # RETRY DEMO FOR HOURS 8-9 REVIEW
            # ==================================================
            # REMOVE OR COMMENT THIS BLOCK AFTER DEMO
            # ==================================================

            if attempt < 2:

                raise Exception(
                    "Simulated Failure"
                )

            result = llm.invoke(
                prompt
            )

            retry_log.append(
                "Success"
            )

            return (
                result.content,
                retry_log
            )

        except Exception as ex:

            error_message = (
                f"Attempt {attempt + 1} failed: {str(ex)}"
            )

            retry_log.append(
                error_message
            )

            logger.error(
                error_message
            )

            attempt += 1

            time.sleep(1)

    return (
        "Retry Limit Reached",
        retry_log
    )

# ==========================================================
# LLM NODE
# ==========================================================
# LangChain
#      ↓
# Claude API
#      ↓
# Claude LLM
# ==========================================================

def llm_node(state):

    prompt = f"""
    User Prompt:
    {state['prompt']}

    Tool Used:
    {state['tool']}

    Tool Result:
    {state['tool_result']}

    Explain clearly.
    """

    response, retry_log = (
        call_llm_with_retry(prompt)
    )

    state["response"] = response

    state["retry_log"] = retry_log

    return state

# ==========================================================
# LANGGRAPH
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
# STREAMLIT
# ==========================================================

st.set_page_config(
    page_title="Hours 8-9 Harness Middleware"
)

st.title(
    "🛡️ Hours 8-9 Harness Middleware"
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
✅ Middleware
✅ Logging
✅ Retry Logic
✅ Guardrails
✅ Error Handling
"""
)

prompt = st.text_input(
    "Enter Prompt",
    "What is today's date?"
)

if st.button(
    "Run Harness"
):

    try:

        # ==================================================
        # MIDDLEWARE CHAIN
        # ==================================================

        validate_input(
            prompt
        )

        policy_check(
            prompt
        )

        # ==================================================
        # LANGGRAPH EXECUTION
        # ==================================================

        result = graph.invoke(
            {
                "prompt": prompt
            }
        )

        # ==================================================
        # RESPONSE
        # ==================================================

        st.subheader(
            "Response"
        )

        st.write(
            result["response"]
        )

        # ==================================================
        # TOOL DETAILS
        # ==================================================

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

        # ==================================================
        # LOGGING + RETRY WRAPPER OUTPUT
        # ==================================================
        # Visible browser demonstration of:
        #
        # ✅ Logging
        # ✅ Retry Wrapper
        # ==================================================

        st.subheader(
            "Middleware Execution Log"
        )

        st.code(
            "\n".join(
                result["retry_log"]
            )
        )

        # ==================================================
        # HARNESS FLOW
        # ==================================================

        st.subheader(
            "Harness Flow"
        )

        st.code(
            """
Browser
 ↓
Guardrail Validation
 ↓
Policy Middleware
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
Retry Wrapper
 ↓
Logging
 ↓
LangSmith
 ↓
Response
"""
        )

    except Exception as ex:

        st.error(
            f"Exception Handling Triggered: {str(ex)}"
        )