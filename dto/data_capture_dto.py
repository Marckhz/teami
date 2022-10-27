from pydantic import BaseModel, validator

class DataCaptureDTO(BaseModel):
    """Object to Make the valiidations
    It wont matter if add floats or string number
    This object will parse it. Atm we are not throwing.

    Raises
    ------
    ValueError if number is lower than zero
    """
    
    value: int = 0

    class Config:
        validate_assignment = True

    @validator('value', always=True)
    def parse_value(cls, value) -> int:
        if value < 0:
            raise ValueError("Element can't be lowe than zero")
        return value
