from pydantic import BaseModel
from typing import List


class AnswerResponse(BaseModel):
    answer: str
    confidence_level: int
    path_answer: str
    follow_up_questions: List[str]


print(AnswerResponse.model_json_schema())