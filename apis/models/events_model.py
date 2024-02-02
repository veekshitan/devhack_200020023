from pydantic import BaseModel, Field


class EventsModel(BaseModel):
    roll_number:str = Field(...)
    name:str = Field(...)
    description:str = Field(...)
    image:str=Field(...)
    website_link:str = Field(...)
    sub_events:dict
    