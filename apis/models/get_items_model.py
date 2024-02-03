from pydantic import BaseModel, Field

class ItemsModel(BaseModel):
    category:str = Field(...)