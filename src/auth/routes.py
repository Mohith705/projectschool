from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from .dependencies import AccessTokenBearer
from .service import AuthService
from src.db.main import get_session
from sqlmodel.ext.asyncio.session import AsyncSession
from .schemas import SchoolUserCreateModel, SchoolUser, SchoolUserLoginModel
from .utils import verify_password
from fastapi.responses import JSONResponse

auth_router = APIRouter()
auth_service = AuthService()

auth_checker = Depends(AccessTokenBearer())

@auth_router.get("/")
async def get_all_users(session: AsyncSession = Depends(get_session)):
    return await auth_service.get_all_users(session)

@auth_router.post("/signup")
async def create_user_account(user_data: SchoolUserCreateModel, session: AsyncSession = Depends(get_session)):
    mobileno = user_data.mobilenumber
    user_exists = await auth_service.is_user_exists(mobileno, session)
    if user_exists:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")
    new_user = await auth_service.create_user(user_data, session)
    return {
        "message": "Account Created!",
        "user": new_user
    }

@auth_router.post("/login")
async def login_users(login_data: SchoolUserLoginModel, session: AsyncSession = Depends(get_session)):
    mobileno = login_data.mobilenumber
    password = login_data.password
    user = await auth_service.get_user_by_mobileno(mobileno, session)
    
    if user is not None:
        password_valid = verify_password(password, user.password_hash)
        if password_valid:
            return JSONResponse(
                content={
                    "message": "Login Successful",
                    "user": {
                        "mobileno": user.mobilenumber,
                        "uid": str(user.uid)
                    }
                }
            )
        
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Credentials")