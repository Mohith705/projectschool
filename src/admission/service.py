from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.models import ParentDetails, AdmissionDetails
from .schemas import ParentCreateModel
from fastapi import HTTPException, status
from src.auth.utils import generate_password_hash
from sqlmodel import select, desc

class AdmissionService:
    async def get_all_admissions(self, session: AsyncSession):
        statement = select(AdmissionDetails).order_by(desc(AdmissionDetails.created_at))
        result = await session.exec(statement)
        return result.all()

    async def create_parent(self, parent_data: ParentCreateModel, session: AsyncSession):
        parent_data_dict = parent_data.model_dump()
        new_parent = ParentDetails(**parent_data_dict)
        hashed_password = generate_password_hash(parent_data_dict['parentpassword'])
        new_parent.parentpassword = hashed_password
        session.add(new_parent)
        await session.commit()
        return new_parent