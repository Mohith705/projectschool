from sqlmodel import select, desc
from src.db.models import SchoolUser
from .schemas import SchoolUserCreateModel
from sqlmodel.ext.asyncio.session import AsyncSession
from .utils import generate_password_hash, verify_password

class AuthService:
    async def get_all_users(self, session: AsyncSession):
        statement = select(SchoolUser).order_by(desc(SchoolUser.created_at))
        result = await session.exec(statement)  
        return result.all()  
    
    async def get_user_by_mobileno(self, mobileno: str, session: AsyncSession):
        statement = select(SchoolUser).where(SchoolUser.mobilenumber == mobileno)
        result = await session.exec(statement)
        user = result.first()
        return user
    
    async def is_user_exists(self, mobileno: str, session: AsyncSession):
        user = await self.get_user_by_mobileno(mobileno, session)
        return True if user is not None else False
    
    async def create_user(self, user_data: SchoolUserCreateModel, session: AsyncSession):
        user_data_dict = user_data.model_dump()
        new_user = SchoolUser(**user_data_dict)
        hashed_password = generate_password_hash(user_data_dict['password'])
        new_user.password_hash = hashed_password
        new_user.role = 'teacher'

        session.add(new_user)
        await session.commit()
        return new_user