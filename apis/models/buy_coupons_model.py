from pydantic import BaseModel, Field

class BuyCouponsModel(BaseModel):
    roll_no:str = Field(...)
    category:str = Field(...)