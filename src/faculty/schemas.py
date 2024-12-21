from pydantic import BaseModel
import uuid

class FacultyDetailsSchema(BaseModel):
    uid: uuid.UUID
    firstname: str
    lastname: str
    imgurl: str
    phonenumber: str
    subject: str
    mail: str
    educationdetails: str
    about: str

class UploadFacultyDetails(BaseModel):
    firstname: str
    lastname: str
    imgurl: str
    phonenumber: str
    subject: str
    mail: str
    educationdetails: str
    about: str