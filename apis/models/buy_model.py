from pydantic import BaseModel, Field

class UserBuyModel(BaseModel):
    roll_number:str = Field(...)