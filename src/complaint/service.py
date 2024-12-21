from sqlmodel.ext.asyncio.session import AsyncSession
from .schemas import ComplaintCreateSchema, ComplaintUpdateSchema
from src.db.models import ComplaintTable
from sqlmodel import select, desc
from fastapi.responses import JSONResponse
from fastapi import HTTPException, status

class ComplaintService:
    async def create_complaint(self, complaint_data: ComplaintCreateSchema, session: AsyncSession):
        complaint_dict = complaint_data.model_dump()
        new_complaint = ComplaintTable(**complaint_dict)
        session.add(new_complaint)
        await session.commit()
        return new_complaint
    
    async def get_complaint(self, session: AsyncSession):
        statement = select(ComplaintTable).order_by(desc(ComplaintTable.created_at))
        result = await session.exec(statement)
        return result.all()
    
    async def delete_complaint(self, uid: str, session: AsyncSession):
        statement = select(ComplaintTable).where(ComplaintTable.uid == uid)
        result = await session.exec(statement)
        complaint = result.first()
        await session.delete(complaint)
        await session.commit()
        return JSONResponse(content={"message": "Complaint deleted successfully"}, status_code=status.HTTP_200_OK)
    
    async def update_complaint(self, uid: str, complaint_data: ComplaintUpdateSchema, session: AsyncSession):
        statement = select(ComplaintTable).where(ComplaintTable.uid == uid)
        result = await session.exec(statement)
        complaint = result.first()
        if not complaint:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Complaint not found")
        complaint_dict = complaint_data.model_dump()
        for key, value in complaint_dict.items():
            setattr(complaint, key, value)
        await session.commit()
        return complaint