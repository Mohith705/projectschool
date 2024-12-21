from fastapi import APIRouter, HTTPException, Depends
from src.db.main import get_session
from sqlmodel.ext.asyncio.session import AsyncSession
from .service import TimeTableService
from .schemas import TimeTableSchema

timetable_router = APIRouter()
timetable_service = TimeTableService()

@timetable_router.get("/")
async def get_full_timetable(session: AsyncSession = Depends(get_session)):
    return await timetable_service.getfull_timetable(session)

@timetable_router.get("/{classno}/{classsection}")
async def get_timetable_by_classsection(classno: int, classsection: str, session: AsyncSession = Depends(get_session)):    
    return await timetable_service.gettimetable_by_classsection(classno, classsection, session)

@timetable_router.get("/{classno}")
async def get_timetable_by_classno(classno: int, session: AsyncSession = Depends(get_session)):
    return await timetable_service.gettimetable_by_classno(classno, session)

@timetable_router.post("/")
async def createorupdate_timetable(timetable_data: TimeTableSchema, session: AsyncSession = Depends(get_session)):
    return await timetable_service.create_update_timetable(timetable_data, session)

@timetable_router.delete("/{classno}/{classsection}")
async def reset_timetable(classno: int, classsection: str, session: AsyncSession = Depends(get_session)):
    return await timetable_service.reset_timetable(classno, classsection, session)

@timetable_router.delete("/{classno}/{classsection}/{day}/{period}")
async def delete_timetable_entry(classno: int, classsection: str, day: str, period: int, session: AsyncSession = Depends(get_session)):
    return await timetable_service.delete_timetable_entry(classno, classsection, day, period, session)