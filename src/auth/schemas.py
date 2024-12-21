from pydantic import BaseModel, Field
import uuid
from datetime import datetime

class SchoolUser(BaseModel):
    uid: uuid.UUID
    username: str
    mobilenumber: str
    password_hash: str = Field(exclude=True)
    designation: str
    created_at: datetime
    updated_at: datetime

class SchoolUserCreateModel(BaseModel):
    username: str
    mobilenumber: str
    password: str
    designation: str

class SchoolUserLoginModel(BaseModel):
    mobilenumber: str
    password: str