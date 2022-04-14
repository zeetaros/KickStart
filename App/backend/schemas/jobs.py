from typing import Optional
from pydantic import BaseModel
from datetime import date, datetime


# Shared properties
class JobBase(BaseModel):
     title: Optional[str] = None
     company : Optional[str] = None
     company_url : Optional[str] = None
     location : Optional[str] = "Remote"
     description : Optional[str] = None
     date_posted : Optional[date] = datetime.now().date()


class JobCreate(JobBase):
     """
     Used to validate data while creating a job
     """
     title: str
     company: str
     location: str
     description: str


class ShowJob(JobBase):
     """
     Used to format the response to not have id, owner_id etc.
     """
     title: str
     company: str
     company_url: Optional[str]
     location: str
     date_posted: date
     description: Optional[str]

     class Config():
          """
          Convert non-dict object to json
          """
          orm_mode = True