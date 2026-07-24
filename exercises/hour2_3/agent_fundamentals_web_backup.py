from dotenv import load_dotenv
import os
import datetime
import streamlit as st
from anthropic import Anthropic

# -------------------------------------
# Load Configuration
# -------------------------------------

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")

# -------------------------------------
# Guardrail
# -------------------------------------

if not api_key:
    st.error("Claude API Key Not Found")
    st.stop()

# -------------------------------------
# Browser Configuration
# -------------------------------------

st.set_page_config(
    page_title="Hours 2-3 Agent Fundamentals"
)

st.title("🤖 Hours 2-3 Agentic Framework Fundamentals")

# -------------------------------------
# Create Claude Client
# -------------------------------------

client = Anthropic(
    api_key=api_key
)

st.success("Claude API Connected")

# -------------------------------------
# Tools
# -------------------------------------

def get_current_date():
    return str(datetime.date.today())

def calculate(expression):
    try:
        return str(eval(expression))
    except:
        return "Invalid calculation."

# -------------------------------------
# State
# -------------------------------------

user_prompt = st.text_area(
    "Enter Prompt",
    "What is today's date?"
)

# -------------------------------------
# Agent Loop
# -------------------------------------

if st.button("Run Agent"):

    tool_result = ""

    # Tool Selection
    if "date" in user_prompt.lower():

        tool_result = get_current_date()

        reasoning = (
            f"Tool Used: Date Tool\n"
            f"Date Result: {tool_result}"
        )

    elif any(op in user_prompt for op in ["+", "-", "*", "/"]):

        tool_result = calculate(user_prompt)

        reasoning = (
            f"Tool Used: Calculator Tool\n"
            f"Calculation Result: {tool_result}"
        )

    else:

        reasoning = (
            "No Tool Required."
        )

    # Claude API Call

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=300,
        messages=[
            {
                "role": "user",
                "content":
                f"""
                User Request:
                {user_prompt}

                Tool Information:
                {reasoning}

                Explain the answer clearly.
                """
            }
        ]
    )

    st.subheader("Agent Response")

    st.write(
        response.content[0].text
    )

    st.subheader("Agent Trace")

    st.code(reasoning)