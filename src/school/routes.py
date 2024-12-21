import cloudinary.uploader
from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, status
from src.db.main import get_session
from sqlmodel.ext.asyncio.session import AsyncSession
from src.school.service import SchoolService
import cloudinary
from src.config import Config
from fastapi.responses import JSONResponse
from .schemas import UploadSchoolDetails

school_router = APIRouter()
school_service = SchoolService()

@school_router.get("/")
async def get_school_details(session: AsyncSession = Depends(get_session)):
    return await school_service.get_school_details(session)

@school_router.post("/uploadimg")
async def upload_images(file: UploadFile = File(...)):
    try:
        upload_result = cloudinary.uploader.upload(file.file, folder="projectschool/schoolimages/")
        image_url = upload_result.get("secure_url")
        if not image_url:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to get image URL in school images")
        
        return JSONResponse(
            content={
                "message": "Image uploaded successfully",
                "image_url": image_url
            },
            status_code=status.HTTP_200_OK
        )
    
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error uploading image in school images: {str(e)}")
    
@school_router.post("/")
async def upload_school_data(schooldata: UploadSchoolDetails, session: AsyncSession = Depends(get_session)):
    return await school_service.upload_school_details(schooldata, session)