from fastapi import APIRouter, Depends
from .service import EventsService
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session
from .schemas import EventSchema

events_router = APIRouter()
events_service = EventsService()

@events_router.get("/")
async def get_all_events(session: AsyncSession = Depends(get_session)):
    return await events_service.get_all_events(session)

@events_router.post("/")
async def createupdate_event(event_data: EventSchema, session: AsyncSession = Depends(get_session)):
    return await events_service.create_update_event(event_data, session)

@events_router.delete("/{eventnumber}")
async def delete_event(eventnumber: int, session: AsyncSession = Depends(get_session)):
    return await events_service.delete_event(eventnumber, session)