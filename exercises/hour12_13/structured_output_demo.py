from pydantic import BaseModel
from typing import List


class AnswerResponse(BaseModel):
    answer: str
    confidence_level: int
    path_answer: str
    follow_up_questions: List[str]


response = AnswerResponse(
    answer="LangChain is a framework for building LLM applications.",
    confidence_level=95,
    path_answer="Knowledge Base -> LangChain Definition",
    follow_up_questions=[
        "What is LangGraph?",
        "What is LangSmith?"
    ]
)

print(response.model_dump_json(indent=4))