from pydantic import BaseModel
from typing import List


class AnswerResponse(BaseModel):
    answer: str
    confidence_level: int
    path_answer: str
    follow_up_questions: List[str]


question = input("Ask a question: ")

response = AnswerResponse(
    answer=f"Response for: {question}",
    confidence_level=90,
    path_answer="Knowledge Base",
    follow_up_questions=[
        "Would you like more details?",
        "Would you like examples?"
    ]
)

print(response.model_dump_json(indent=4))