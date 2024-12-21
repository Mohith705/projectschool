from pydantic import BaseModel
import uuid

class SchoolDetailsSchema(BaseModel):
    uid: uuid.UUID
    schoolname: str
    schoolinfo: str
    founderimg: str
    foundername: str
    schoolimages: list[str]
    associated_people: list[dict[str, str]]

class AssociatedPerson(BaseModel):
    personname: str
    personinfo: str
    personstudies: str

class UploadSchoolDetails(BaseModel):
    schoolname: str
    schoolinfo: str
    founderimg: str
    foundername: str
    schoolimages: list[str]
    associated_people: list[AssociatedPerson]