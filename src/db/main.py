from sqlmodel import create_engine
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from src.config import Config
from sqlalchemy.orm import sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi import Request, Depends, HTTPException, status
from typing import AsyncGenerator

db_engines = {}

def get_async_engine(schoolname: str) -> AsyncEngine:
    """
    Get or create a database engine dynamically for the given schoolname.
    """
    if schoolname not in db_engines:
        db_url = Config.DATABASE_URL.format( db_name = schoolname )
        db_engines[schoolname] = create_async_engine(db_url, echo=False, pool_pre_ping=True)
    return db_engines[schoolname]

async def get_session(request: Request) -> AsyncGenerator[AsyncSession, None]:
    """
    Get a database session dynamically based on the schoolname in headers.
    """
    schoolname = request.headers.get("schoolname") 
    if not schoolname:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The 'schoolname' header is missing. Please include it in the request headers."
        )

    async_engine = get_async_engine(schoolname) 

    AsyncSessionLocal = sessionmaker(
        bind=async_engine,
        class_=AsyncSession,
        expire_on_commit=False
    )

    async with AsyncSessionLocal() as session:
        yield session