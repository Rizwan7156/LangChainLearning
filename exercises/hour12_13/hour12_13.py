"""
Hours 12-13

Structured Output

Demonstrates

✅ LLM
✅ Claude API
✅ LangChain
✅ LangGraph
✅ LangSmith
✅ Separate Agent
✅ Tools
✅ Pydantic
✅ JSON Schema
✅ Validation
✅ Structured Output
✅ Browser UI
"""

import os
import json
import streamlit as st
from dotenv import load_dotenv

# ==========================================================
# LANGSMITH
# ==========================================================

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Hours12-13-StructuredOutput"

# ==========================================================
# ENVIRONMENT
# ==========================================================

load_dotenv()

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
# AGENT
# ==========================================================

from agents.structured_output_agent import (
    StructuredOutputAgent,
    AnswerSchema
)

agent = StructuredOutputAgent(
    llm
)

# ==========================================================
# TOOL
# ==========================================================
# Simple validation tool
# ==========================================================

def validation_tool(json_text):

    try:

        json_text = json_text.replace(
            "```json",
            ""
        )

        json_text = json_text.replace(
            "```",
            ""
        )

        json_text = json_text.strip()

        data = json.loads(
            json_text
        )

        validated = AnswerSchema(
            **data
        )

        return validated

    except Exception as ex:

        raise ValueError(
            f"Schema Validation Failed: {str(ex)}"
        )

# ==========================================================
# LANGGRAPH
# ==========================================================

from langgraph.graph import (
    StateGraph,
    END
)

# ==========================================================
# AGENT NODE
# ==========================================================

def agent_node(state):

    response = agent.execute(
        state["question"]
    )

    state["raw_json"] = response

    return state

# ==========================================================
# VALIDATION NODE
# ==========================================================



# ==========================================================
# BUILD GRAPH# ==========================================================
# VALIDATION NODE
# ==========================================================

def validation_node(state):

    st.subheader(
        "Raw Claude Response"
    )

    st.code(
        state["raw_json"]
    )

    validated = validation_tool(
        state["raw_json"]
    )

    state["validated"] = validated

    return state

# ==========================================================

workflow = StateGraph(dict)

workflow.add_node(
    "agent",
    agent_node
)

workflow.add_node(
    "validation",
    validation_node
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
    END
)

graph = workflow.compile()

# ==========================================================
# STREAMLIT UI
# ==========================================================

st.set_page_config(
    page_title="Hours 12-13 Structured Output"
)

st.title(
    "📋 Hours 12-13 Structured Output"
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
✅ Tool
✅ Pydantic
✅ JSON Schema
✅ Validation
✅ Structured Output
"""
)

question = st.text_area(
    "Enter Question",
    "What is LangChain?"
)

if st.button(
    "Generate Structured Output"
):

    try:

        result = graph.invoke(
            {
                "question": question
            }
        )

        validated = result[
            "validated"
        ]

        st.subheader(
            "Validated JSON"
        )

        st.json(
            validated.model_dump()
        )

        st.subheader(
            "Execution Flow"
        )

        st.code(
            """
Browser
 ↓
Separate Agent
 ↓
Claude API
 ↓
JSON Output
 ↓
Validation Tool
 ↓
Pydantic Schema
 ↓
Validated Response
"""
        )

    except Exception as ex:

        st.error(
            str(ex)
        )