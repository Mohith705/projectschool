from sqlmodel import SQLModel, Field, Column, Relationship, JSON
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime, date
import uuid
from typing import List, Optional, Dict
from sqlalchemy import Enum

class SchoolUser(SQLModel, table=True):
    __tablename__ = "schooluser"
    uid: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID,
            nullable=False,
            primary_key=True,
            default=uuid.uuid4
        )
    )
    username: str
    mobilenumber: str
    password_hash: str = Field(exclude=True)
    designation: str
    role: str = Field(
        sa_column=Column(
            pg.VARCHAR,
            nullable=False,
            server_default="teacher"
        )
    )
    created_at: datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP,
            default=datetime.now,
        )
    )
    updated_at: datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP,
            default=datetime.now,
        )
    )

    def __repr__(self):
        return f"<Teacher {self.username}>"
    
class AdmissionDetails(SQLModel, table=True):
    __tablename__ = "admissiondetails"
    uid: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID,
            nullable=False,
            primary_key=True,
            default=uuid.uuid4
        )
    )
    studentname: str
    address: str
    govtprooftype: str
    govtid: str
    caste: str
    dob: date
    joiningdate: date
    classno: int
    classsection: str
    created_at: datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP,
            default=datetime.now,
        )
    )
    updated_at: datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP,
            default=datetime.now,
        )
    )
    parent_uid: Optional[uuid.UUID] = Field(
        foreign_key="parentdetails.uid"
    ) 

    parent: Optional["ParentDetails"] = Relationship(
        back_populates="children"
    )  

class ParentDetails(SQLModel, table=True):
    __tablename__ = "parentdetails"
    uid: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID,
            nullable=False,
            primary_key=True,
            default=uuid.uuid4
        )
    )
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
    parentpassword: str = Field(exclude=True)

    children: List[AdmissionDetails] = Relationship(
        back_populates="parent"
    )  

class FacultyDetails(SQLModel, table=True):
    __tablename__ = "facultydetails"
    uid: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID,
            nullable=False,
            primary_key=True,
            default=uuid.uuid4
        )
    )
    firstname: str
    lastname: str
    imgurl: str
    phonenumber: str
    subject: str
    mail: str
    educationdetails: str
    about: str
    created_at: datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP,
            default=datetime.now,
        )
    )
    updated_at: datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP,
            default=datetime.now,
        )
    )

    timetable: List["TimeTable"] = Relationship(
        back_populates="facutly"
    )

class SchoolDetails(SQLModel, table=True):
    __tablename__="schooldetails"
    uid: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID,
            nullable=False,
            primary_key=True,
            default=uuid.uuid4
        )
    )
    schoolname: str
    schoolinfo: str
    founderimg: str
    foundername: str
    schoolimages: List[str] = Field(
        sa_column=Column(
            pg.ARRAY(pg.VARCHAR),
            nullable=True,
            default=[]
        )
    )
    associated_people: List[Dict[str, str]] = Field(
        sa_column=Column(
            pg.JSONB,
            nullable=True,
            default=[]
        )
    )
    created_at: datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP,
            default=datetime.now
        )
    )
    updated_at: datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP,
            default=datetime.now
        )
    )

class TimeTable(SQLModel, table=True):
    __tablename__ = "timetable"
    uid: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID,
            nullable=False,
            primary_key=True,
            default=uuid.uuid4
        )
    )
    classno: int
    classsection: str
    day: str
    period: int
    subject: str
    facultyuid: Optional[uuid.UUID] = Field(default=None, foreign_key="facultydetails.uid")
    created_at: datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP,
            default=datetime.now
        )
    )
    updated_at: datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP,
            default=datetime.now
        )
    )

    facutly: Optional[FacultyDetails] = Relationship(
        back_populates="timetable"
    )

class EventsTable(SQLModel, table=True):
    __tablename__ = "eventstable"
    uid: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID,
            nullable=False,
            primary_key=True,
            default=uuid.uuid4
        )
    )
    eventnumber: int = Field(
        sa_column=Column(
            pg.INTEGER,
            nullable=False,
            unique=True,
            autoincrement=True
        )
    )
    eventname: str
    eventfromdate: date
    eventtodate: date
    eventfromtime: str
    eventtotime: str
    eventdescription: str
    eventimages: List[str] = Field(
        sa_column=Column(
            pg.ARRAY(pg.VARCHAR),
            nullable=True,
            default=[]
        )
    )
    created_at: datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP,
            default=datetime.now
        )
    )
    updated_at: datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP,
            default=datetime.now
        )
    )

class LeaveTable(SQLModel, table=True):
    __tablename__ = "leavetable"
    uid: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID,
            nullable=False,
            primary_key=True,
            default=uuid.uuid4
        )
    )
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
    status: str 
    comments: Optional[str] = None
    created_at: datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP,
            default=datetime.now
        )
    )
    updated_at: datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP,
            default=datetime.now
        )
    )

class HomeworkTable(SQLModel, table=True):
    __tablename__ = "homeworktable"
    uid: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID,
            nullable=False,
            primary_key=True,
            default=uuid.uuid4
        )
    )
    classno: int
    classsection: str
    name: str
    homeworkdate: date
    subsections: List[dict] = Field(
        sa_column=Column(
            JSON,
            default=list  
        )
    )
    created_at: datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP,
            default=datetime.now
        )
    )
    updated_at: datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP,
            default=datetime.now
        )
    )

class ComplaintTable(SQLModel, table=True):
    __tablename__ = "complaintable"
    uid: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID,
            nullable=False,
            primary_key=True,
            default=uuid.uuid4
        )
    )
    studentname: str
    parentname: str
    parentmobilenumber: str
    classno: int
    classsection: str
    complaintdate: date
    complaintdescription: str
    suggestion: str
    created_at: datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP,
            default=datetime.now
        )
    )
    updated_at: datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP,
            default=datetime.now
        )
    )

class FeedbackTable(SQLModel, table=True):
    __tablename__ = "feedbacktable"
    uid: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID,
            nullable=False,
            primary_key=True,
            default=uuid.uuid4
        )
    )
    studentname: str
    parentname: str
    parentmobilenumber: str
    classno: int
    classsection: str
    feedbackdate: date
    rating: int
    feedbackdescription: str
    created_at: datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP,
            default=datetime.now
        )
    )
    updated_at: datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP,
            default=datetime.now
        )
    )