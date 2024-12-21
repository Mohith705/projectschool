from pydantic import BaseModel
import uuid
from datetime import datetime, date

class AdmissionDetails(BaseModel):
    uid: uuid.UUID
    studentname: str
    address: str
    govtprooftype: str
    govtid: str
    caste: str
    dob: date
    joiningdate: date
    classno: int
    classsection: str

class ParentDetails(BaseModel):
    uid: uuid.UUID
    fathername: str
    mothername: str
    fathergraduation: str
    mothergraduation: str
    fatherdesignation: str
    motherdesignation: str
    parentgovtprooftype: str
    parentgovtid: str
    parentmobilenumber: str
    guardiannumber: str
    parentpassword: str

class ParentCreateModel(BaseModel):
    fathername: str
    mothername: str
    fathergraduation: str
    mothergraduation: str
    fatherdesignation: str
    motherdesignation: str
    parentgovtprooftype: str
    parentgovtid: str
    parentmobilenumber: str
    guardiannumber: str
    parentpassword: str