from pydantic import BaseModel
from datetime import date

class FeedbackCreateSchema(BaseModel):
    feedbackdescription: str
    rating: int
    studentname: str
    parentname: str
    classno: int
    classsection: str
    parentmobilenumber: str
    feedbackdate: date