from fastapi import APIRouter, Depends
from .service import HomeWork2Service
from .schemas import HomeworkCreateSchema
from src.db.main import get_session
from sqlmodel.ext.asyncio.session import AsyncSession
from datetime import date
import uuid

homework_router = APIRouter()
homework_service = HomeWork2Service()

@homework_router.post("/")
async def create_homework(homework_data: HomeworkCreateSchema, session: AsyncSession = Depends(get_session)):
    return await homework_service.create_homework(homework_data, session)

@homework_router.get("/")
async def get_homeworks(session: AsyncSession = Depends(get_session)):
    return await homework_service.get_homework(session)

@homework_router.get("/{todaydate}")
async def get_homeworks_by_date(todaydate: date, session: AsyncSession = Depends(get_session)):
    return await homework_service.get_homework_by_date(todaydate, session)

@homework_router.get("/{homework_uid}")
async def get_homework_by_uid(homework_uid: uuid.UUID, session: AsyncSession = Depends(get_session)):
    return await homework_service.get_homework_by_uid(homework_uid, session)
