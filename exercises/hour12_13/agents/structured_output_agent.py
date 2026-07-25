"""
Hours 12-13

Structured Output Agent

Demonstrates

✅ Agent (Separate Program)
✅ Pydantic Schema
✅ Validation
✅ JSON Contract
✅ Claude API
✅ LangChain
"""

from pydantic import BaseModel, Field
from typing import List


# ==========================================================
# PYDANTIC SCHEMA
# ==========================================================
# Structured Output Contract
# ==========================================================

class AnswerSchema(BaseModel):

    answer: str = Field(
        description="Main answer"
    )

    confidence_level: int = Field(
        description="Confidence from 1-100"
    )

    path_answer: List[str] = Field(
        description="Reasoning steps"
    )

    follow_up_questions: List[str] = Field(
        description="Suggested follow-up questions"
    )


# ==========================================================
# AGENT
# ==========================================================
# Separate reusable Agent
# ==========================================================

class StructuredOutputAgent:

    def __init__(self, llm):

        self.llm = llm

    def execute(self, user_question):

        prompt = f"""
        Answer the question and return ONLY valid JSON.

        Required Schema:

        {{
          "answer": "text",
          "confidence_level": 90,
          "path_answer": [
            "step1",
            "step2"
          ],
          "follow_up_questions": [
            "question1",
            "question2"
          ]
        }}

        Question:
        {user_question}
        """

        response = self.llm.invoke(
            prompt
        ).content

        return response