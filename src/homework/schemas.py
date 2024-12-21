from pydantic import BaseModel
from typing import List, Dict
from datetime import date

class SubsectionSchema(BaseModel):
    name: str
    details: List[str]  # List of strings for subsection details

class HomeworkCreateSchema(BaseModel):
    classno: int
    classsection: str
    name: str
    homeworkdate: date
    subsections: List[SubsectionSchema]  # List of subsections
