from pydantic import BaseModel, Field


class SellModel(BaseModel):
    roll_number:str = Field(...)
    category:str = Field(...)
    item_name:str = Field(...)
    cost:str = Field(...)
    images:str=Field(...)
