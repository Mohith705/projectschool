from pydantic import BaseModel

class EventSchema(BaseModel):
    eventnumber: int
    eventname: str
    eventfromdate: str
    eventtodate: str
    eventfromtime: str
    eventtotime: str
    eventdescription: str