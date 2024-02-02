from pydantic import BaseModel, Field

class BuyCouponsModel(BaseModel):
    roll_number:str = Field(...)
    good_number:str = Field(...)