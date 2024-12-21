from fastapi import APIRouter, Depends, HTTPException
from .service import LeaveService
from .schemas import LeaveCreateSchema, LeaveUpdateSchema, LeaveContentUpdateSchema
from src.db.main import get_session
from sqlmodel.ext.asyncio.session import AsyncSession
from uuid import UUID
from typing import Optional

leave_router = APIRouter()
leave_service = LeaveService()

@leave_router.post("/")
async def create_leave_request(leave_data: LeaveCreateSchema, session: AsyncSession = Depends(get_session)):
    return await leave_service.create_leave_request(leave_data, session)

@leave_router.get("/")
async def get_leave_requests(session: AsyncSession = Depends(get_session)):
    return await leave_service.get_leave_requests(session)

@leave_router.put("/{leave_uid}")
async def update_leave_status_and_comments(leave_uid: UUID, leave_data: LeaveUpdateSchema, session: AsyncSession = Depends(get_session)):
    try:
        return await leave_service.update_leave_status_and_comments(leave_uid, leave_data, session)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@leave_router.put("/content/{leave_uid}")
async def update_leave_content(leave_uid: UUID, leave_data: LeaveContentUpdateSchema, session: AsyncSession = Depends(get_session)):
    try:
        return await leave_service.update_leave_content(leave_uid, leave_data, session)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@leave_router.delete("/{leave_uid}")
async def delete_leave_request(leave_uid: UUID, session: AsyncSession = Depends(get_session)):
    try:
        return await leave_service.delete_leave_request(leave_uid, session)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
