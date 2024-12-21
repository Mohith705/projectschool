from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.models import SchoolDetails
from sqlmodel import select, desc
from .schemas import UploadSchoolDetails

class SchoolService:
    async def get_school_details(self, session: AsyncSession):
        statement = select(SchoolDetails).order_by(desc(SchoolDetails.created_at))
        result = await session.exec(statement)
        return result.all()
    
    async def upload_school_details(self, schooldata: UploadSchoolDetails, session: AsyncSession):
        schooldata_dict = schooldata.model_dump()
        new_schooldata = SchoolDetails(**schooldata_dict)
        session.add(new_schooldata)
        await session.commit()
        return new_schooldata