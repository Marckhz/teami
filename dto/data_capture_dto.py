from pydantic import BaseModel, validator

class DataCaptureDTO(BaseModel):
    
    value: int = 0

    class Config:
        validate_assignment = True

    @validator('value', always=True)
    def parse_value(cls, value) -> int:
        if value < 0:
            raise ValueError("Element can't be lowe than zero")
        return value
