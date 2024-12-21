from .schemas import FeedbackCreateSchema
from src.db.models import FeedbackTable
from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi.responses import JSONResponse
from fastapi import status
from sqlmodel import select, desc

class FeedbackService:
    async def create_feedback(self, feedback_data: FeedbackCreateSchema, session: AsyncSession):
        feedback_dict = feedback_data.model_dump()
        new_feedback = FeedbackTable(**feedback_dict)
        session.add(new_feedback)
        await session.commit()
        return JSONResponse(content={"message": "Feedback Created Successfully"},  status_code=status.HTTP_201_CREATED)
    
    async def get_feedback(self, session: AsyncSession):
        statement = select(FeedbackTable).order_by(desc(FeedbackTable.created_at))
        feedbacks = await session.exec(statement)
        return feedbacks.all()