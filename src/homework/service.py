from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.models import HomeworkTable
from sqlmodel import select, desc
from datetime import date
import uuid
from .schemas import HomeworkCreateSchema

class HomeWork2Service:
    async def create_homework(self, homework_data: HomeworkCreateSchema, session: AsyncSession):
        # Create a new HomeworkTable entry
        new_homework = HomeworkTable(
            name=homework_data.name,
            classno=homework_data.classno,
            classsection=homework_data.classsection,
            homeworkdate=homework_data.homeworkdate,
            subsections=[
                {"name": subsection.name, "details": subsection.details} 
                for subsection in homework_data.subsections
            ]
        )
        session.add(new_homework)
        await session.commit()
        await session.refresh(new_homework)
        return new_homework

    async def get_homework(self, session: AsyncSession):
        # Get all homework entries
        statement = select(HomeworkTable).order_by(desc(HomeworkTable.created_at))
        homeworks = await session.exec(statement)
        return homeworks.all()

    async def get_homework_by_date(self, todaydate: date, session: AsyncSession):
        # Get homework entries for a specific date
        statement = select(HomeworkTable).where(HomeworkTable.homeworkdate == todaydate).order_by(desc(HomeworkTable.created_at))
        homeworks = await session.execute(statement)
        return homeworks.scalars().all()

    async def get_homework_by_uid(self, homework_uid: uuid.UUID, session: AsyncSession):
        # Get homework details by UID
        statement = select(HomeworkTable).where(HomeworkTable.uid == homework_uid)
        homework = await session.execute(statement)
        return homework.scalar_one_or_none()
