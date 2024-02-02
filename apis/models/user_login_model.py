from pydantic import BaseModel, Field

class UserLoginModel(BaseModel):
    roll_number:str = Field(...)
    password:str = Field(...)