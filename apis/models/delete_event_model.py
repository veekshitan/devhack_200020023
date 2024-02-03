from pydantic import BaseModel, Field

class DeleteEventModel(BaseModel):
    roll_no:str = Field(...)
    name: str = Field(...)