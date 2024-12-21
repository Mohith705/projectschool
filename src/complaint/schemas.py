from pydantic import BaseModel
from datetime import date

class ComplaintCreateSchema(BaseModel):
    studentname: str
    parentname: str
    parentmobilenumber: str
    classno: int
    classsection: str
    complaintdescription: str
    suggestion: str
    complaintdate: date

class ComplaintUpdateSchema(BaseModel):
    complaintdescription: str
    suggestion: str