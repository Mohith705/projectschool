from fastapi import APIRouter, Depends
from .service import ComplaintService
from src.db.main import get_session
from sqlmodel.ext.asyncio.session import AsyncSession
from .schemas import ComplaintCreateSchema, ComplaintUpdateSchema

complaint_router = APIRouter()
complaint_service = ComplaintService()

@complaint_router.post("/")
async def create_complaint(complaint_data: ComplaintCreateSchema, session: AsyncSession = Depends(get_session)):
    return await complaint_service.create_complaint(complaint_data, session)

@complaint_router.get("/")
async def get_complaint(session: AsyncSession = Depends(get_session)):
    return await complaint_service.get_complaint(session)

@complaint_router.delete("/{uid}")
async def delete_complaint(uid: str, session: AsyncSession = Depends(get_session)):
    return await complaint_service.delete_complaint(uid, session)

@complaint_router.put("/{uid}")
async def update_complaint(uid: str, complaint_data: ComplaintUpdateSchema, session: AsyncSession = Depends(get_session)):
    return await complaint_service.update_complaint(uid, complaint_data, session)