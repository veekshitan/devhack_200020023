from fastapi import APIRouter, Depends, Request
from models.events_model import EventsModel
router=APIRouter()

@router.post("/events")
async def add_event(request: EventsModel):
    return add_event(request.roll_number, request.name, request.description,request.image,request.website_link,request.sub_events)
@router.get("/events")
async def add_event(request:Request ):
