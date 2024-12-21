from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.models import FacultyDetails
from sqlmodel import select, desc
from .schemas import UploadFacultyDetails

class FacultyService:
    async def get_all_faculty(self, session: AsyncSession):
        statement = select(FacultyDetails).order_by(desc(FacultyDetails.created_at))
        result = await session.exec(statement)
        return result.all()
    
    async def upload_faculty_data(self, facultydata: UploadFacultyDetails, session: AsyncSession):
        facultydata_dict = facultydata.model_dump()
        new_faculty = FacultyDetails(**facultydata_dict)
        session.add(new_faculty)
        await session.commit()
        return new_faculty