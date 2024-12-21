from fastapi import APIRouter, Depends, File, UploadFile, HTTPException, status
from fastapi.responses import JSONResponse
from .service import FacultyService
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session
import cloudinary
import cloudinary.uploader
from src.config import Config
from .schemas import UploadFacultyDetails

faculty_router = APIRouter()
faculty_service = FacultyService()

cloudinary.config(
    cloud_name=Config.CLOUDINARY_CLOUD_NAME,  
    api_key=Config.CLOUDINARY_API_KEY,  
    api_secret=Config.CLOUDINARY_API_SECRET,  
)

@faculty_router.get("/")
async def get_all_faculty(session: AsyncSession = Depends(get_session)):
    return await faculty_service.get_all_faculty(session)

@faculty_router.post("/uploadimg")
async def upload_image(file: UploadFile = File(...)):
    try:
        upload_result = cloudinary.uploader.upload(file.file, folder="projectschool/")

        image_url = upload_result.get("secure_url")
        if not image_url:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to get image URL")
        
        return JSONResponse(
            content={
                "message": "Image uploaded successfully",
                "image_url": image_url
            },
            status_code=status.HTTP_200_OK
        )

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error uploading image: {str(e)}")

@faculty_router.post("/")
async def upload_faculty_data(facultydata: UploadFacultyDetails, session: AsyncSession = Depends(get_session)):
    return await faculty_service.upload_faculty_data(facultydata, session)