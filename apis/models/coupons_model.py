from pydantic import BaseModel, Field

class CouponsModel(BaseModel):
    roll_no:str = Field(...)
    category:str = Field(...)