from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select, desc, update
from .schemas import LeaveCreateSchema, LeaveUpdateSchema, LeaveContentUpdateSchema
from src.db.models import LeaveTable
import uuid
from datetime import datetime

class LeaveService:
    async def create_leave_request(self, leave_data: LeaveCreateSchema, session: AsyncSession):
        leave_request = LeaveTable(
            studentname=leave_data.studentname,
            parentname=leave_data.parentname,
            parentmobilenumber=leave_data.parentmobilenumber,
            classno=leave_data.classno,
            classsection=leave_data.classsection,
            fromdate=leave_data.fromdate,
            todate=leave_data.todate,
            fromtime=leave_data.fromtime,
            totime=leave_data.totime,
            reason=leave_data.reason,
            place=leave_data.place,
            status="pending"
        )
        session.add(leave_request)
        await session.commit()
        await session.refresh(leave_request)
        return leave_request
    
    async def get_leave_requests(self, session: AsyncSession):
        statement = select(LeaveTable).order_by(desc(LeaveTable.created_at))
        leave_requests = await session.exec(statement)
        return leave_requests.all()

    async def update_leave_status_and_comments(self, leave_uid: uuid.UUID, leave_data: LeaveUpdateSchema, session: AsyncSession):
        statement = select(LeaveTable).where(LeaveTable.uid == leave_uid)
        leave_request = await session.exec(statement)
        leave_request = leave_request.first()
        
        if leave_request:
            leave_request.status = leave_data.status
            leave_request.comments = leave_data.comments
            await session.commit()
            await session.refresh(leave_request)
            return leave_request
        else:
            raise Exception("Leave request not found")

    async def delete_leave_request(self, leave_uid: uuid.UUID, session: AsyncSession):
        statement = select(LeaveTable).where(LeaveTable.uid == leave_uid)
        leave_request = await session.exec(statement)
        leave_request = leave_request.first()
        
        if leave_request:
            await session.delete(leave_request)
            await session.commit()
            return {"message": "Leave request deleted successfully"}
        else:
            raise Exception("Leave request not found")
        
    async def update_leave_content(self, leave_uid: uuid.UUID, leave_data: LeaveContentUpdateSchema, session: AsyncSession):
        statement = select(LeaveTable).where(LeaveTable.uid == leave_uid)
        leave_request = await session.exec(statement)
        leave_request = leave_request.first()

        if not leave_request:
            raise Exception("Leave request not found.")
        
        if leave_request.status != "pending":
            raise Exception("Cannot update leave request. Status is not 'pending'.")

        updated_data = leave_data.model_dump(exclude_unset=True) 
        updated_data["updated_at"] = datetime.now()  

        statement = update(LeaveTable).where(LeaveTable.uid == leave_uid).values(**updated_data)
        await session.exec(statement)
        await session.commit()

        leave_request = await session.get(LeaveTable, leave_uid)
        return leave_request