import typing as tp
from pydantic import BaseModel, EmailStr, Field


from models import Company, ObjectIdStr


class Recruiter(BaseModel):
    id: ObjectIdStr = Field(default_factory=ObjectIdStr, alias="_id")
    company: tp.Optional[Company]
    email: EmailStr
    mobile: int
