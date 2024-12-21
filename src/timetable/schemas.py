from pydantic import BaseModel

class TimeTableSchema(BaseModel):
    classno: int
    classsection: str
    subject: str
    facultyuid: str
    day: str
    period: int