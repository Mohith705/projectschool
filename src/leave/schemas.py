from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

class LeaveSchema(BaseModel):
    studentname: str
    parentname: str
    parentmobilenumber: str
    classno: int
    fromdate: date
    todate: date
    fromtime: Optional[datetime]
    totime: Optional[datetime]
    reason: str
    place: str
    status: str
    comments: Optional[str] = None

class LeaveCreateSchema(BaseModel):
    studentname: str
    parentname: str
    parentmobilenumber: str
    classno: int
    classsection: str
    fromdate: date
    todate: date
    fromtime: Optional[datetime]
    totime: Optional[datetime]
    reason: str
    place: str

class LeaveUpdateSchema(BaseModel):
    status: str
    comments: Optional[str] = None

class LeaveContentUpdateSchema(BaseModel):
    fromdate: Optional[date] = None
    todate: Optional[date] = None
    fromtime: Optional[datetime] = None
    totime: Optional[datetime] = None
    reason: Optional[str] = None
    place: Optional[str] = None