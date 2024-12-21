from datetime import datetime
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select, desc
from src.db.models import EventsTable
from .schemas import EventSchema

class EventsService:
    async def get_all_events(self, session: AsyncSession):
        statement = select(EventsTable).order_by(desc(EventsTable.created_at))
        result = await session.exec(statement)
        return result.all()

    async def create_update_event(self, event_data: EventSchema, session: AsyncSession):
        try:
            event_data.eventfromdate = datetime.strptime(event_data.eventfromdate, "%Y-%m-%d").date()
            event_data.eventtodate = datetime.strptime(event_data.eventtodate, "%Y-%m-%d").date()
        except ValueError:
            return {"error": "Invalid date format. Use 'YYYY-MM-DD' for dates."}

        is_exist_statement = select(EventsTable).where(EventsTable.eventnumber == event_data.eventnumber)
        is_exist_result = await session.exec(is_exist_statement)
        is_exist = is_exist_result.first()

        if is_exist:
            is_exist.eventname = event_data.eventname
            is_exist.eventfromdate = event_data.eventfromdate
            is_exist.eventtodate = event_data.eventtodate
            is_exist.eventfromtime = event_data.eventfromtime
            is_exist.eventtotime = event_data.eventtotime
            is_exist.eventdescription = event_data.eventdescription
            await session.commit()
            await session.refresh(is_exist)
            return {"message": "Event updated successfully", "data": event_data}
        else:
            # Create new event
            new_event = EventsTable(
                eventnumber=event_data.eventnumber,
                eventname=event_data.eventname,
                eventfromdate=event_data.eventfromdate,
                eventtodate=event_data.eventtodate,
                eventfromtime=event_data.eventfromtime,
                eventtotime=event_data.eventtotime,
                eventdescription=event_data.eventdescription
            )
            session.add(new_event)
            await session.commit()
            await session.refresh(new_event)
            return {"message": "Event created successfully", "data": event_data}
        
    async def delete_event(self, eventnumber: int, session: AsyncSession):
        statement = select(EventsTable).where(EventsTable.eventnumber == eventnumber)
        result = await session.exec(statement)
        event = result.first()
        if event:
            await session.delete(event)
            await session.commit()
            return {"message": "Event deleted successfully"}
        return {"error": "Event not found"}