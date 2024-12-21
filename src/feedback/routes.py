from fastapi import APIRouter, Depends, HTTPException
from src.db.main import get_session
from .service import FeedbackService
from .schemas import FeedbackCreateSchema

feedback_router = APIRouter()
feedback_service = FeedbackService()

@feedback_router.post("/")
async def create_feedback(feedback_data: FeedbackCreateSchema, session = Depends(get_session)):
    try:
        return await feedback_service.create_feedback(feedback_data, session)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@feedback_router.get("/")
async def get_feedback(session = Depends(get_session)):
    try:
        return await feedback_service.get_feedback(session)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))