from pydantic import BaseModel, ValidationError


class AnswerResponse(BaseModel):
    confidence_level: int


try:

    response = AnswerResponse(
        confidence_level="high"
    )

except ValidationError as ex:

    print("Validation Error")
    print(ex)