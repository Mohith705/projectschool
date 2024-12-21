from fastapi import APIRouter, Depends, HTTPException, status
from .service import AdmissionService
from .schemas import ParentCreateModel
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session
from src.auth.service import AuthService

admission_router = APIRouter()
admission_service = AdmissionService()
auth_service = AuthService()

@admission_router.get("/")
async def get_all_admissions():
    return {"message": "Get all admissions"}

@admission_router.post("/createparent")
async def create_parent(parent_data: ParentCreateModel, session: AsyncSession = Depends(get_session)):
    mobileno = parent_data.parentmobilenumber
    user = await auth_service.get_user_by_mobileno(mobileno, session)
    if user is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Already user exists")
    new_parent = await admission_service.create_parent(
        parent_data, session
    )
    return {
        "message": "Parent Created",
        "details": new_parent
    }