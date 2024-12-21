from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select, desc
from src.db.models import TimeTable
from fastapi import HTTPException, status
from .schemas import TimeTableSchema
from datetime import datetime
from fastapi.encoders import jsonable_encoder
from sqlalchemy.dialects.postgresql import dialect


class TimeTableService:
    async def getfull_timetable(self, session: AsyncSession):
        statement = select(TimeTable).order_by(desc(TimeTable.created_at))
        result = await session.exec(statement)
        return result.all()
    
    async def gettimetable_by_classsection(self, classno: int, classsection: str, session: AsyncSession):
        statement = select(TimeTable).where(TimeTable.classno == classno, TimeTable.classsection == classsection)
        result = await session.exec(statement)

        if not result.all():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Timetable not found for {classno} - {classsection}")
        
        timetable = result.all()
        return timetable
    
    async def gettimetable_by_classno(self, classno: int, session: AsyncSession):
        statement = select(TimeTable).where(TimeTable.classno == classno)
        result = await session.exec(statement)

        if not result.all():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Timetable not found for {classno}")
    
        return result.all()
    
    async def create_update_timetable(self, timetable_data: TimeTableSchema, session: AsyncSession):
        is_exist_statement = select(TimeTable).where(TimeTable.classno == timetable_data.classno, TimeTable.classsection == timetable_data.classsection)
        is_exist_result = await session.exec(is_exist_statement)
        is_exist_entry = is_exist_result.first()

        if is_exist_entry:
            is_exist_entry.subject = timetable_data.subject
            is_exist_entry.facultyuid = timetable_data.facultyuid
            is_exist_entry.day = timetable_data.day
            is_exist_entry.period = timetable_data.period
            is_exist_entry.updated_at = datetime.now()
            session.add(is_exist_entry)
            await session.commit()
            await session.refresh(is_exist_entry)
            return {"message": "Timetable updated successfully", "data": is_exist_entry}
        else:
            new_timetable_dict = timetable_data.model_dump()
            new_timetable = TimeTable(**new_timetable_dict)
            session.add(new_timetable)
            await session.commit()
            return {"message": "Timetable created successfully", "data": new_timetable}
        
    async def reset_timetable(self, classno: int, classsection: str, session: AsyncSession):
        statement = select(TimeTable).where(TimeTable.classno == classno, TimeTable.classsection == classsection)
        result = await session.exec(statement)
        timetable_entries = result.all()

        print(timetable_entries)

        if not timetable_entries:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Timetable not found for {classno} - {classsection}")
        for entry in timetable_entries:
            await session.delete(entry)

        await session.commit()
        return {"message": f"Timetable reset successfully for {classno} - {classsection}"}
    
    async def delete_timetable_entry(self, classno: int, classsection: str, day: str, period: int, session: AsyncSession):
        statement = select(TimeTable).where(TimeTable.classno == classno, TimeTable.classsection == classsection, TimeTable.day == day, TimeTable.period == period)
        result = await session.exec(statement)
        timetable_entry = result.first()

        if not timetable_entry:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Timetable entry not found for {classno} - {classsection} - {day} - {period}")
        
        await session.delete(timetable_entry)
        await session.commit()
        return {"message": f"Timetable entry deleted successfully for {classno} - {classsection} - {day} - {period}"}