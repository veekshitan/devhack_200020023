from pydantic import BaseModel, Field

class DeleteItemModel(BaseModel):
    good_number:str = Field(...)