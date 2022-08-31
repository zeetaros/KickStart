import typing as tp
from datetime import datetime
from bson import ObjectId

from pydantic import Field

from models import ModBaseModel, Company, Attachment, Recruiter, Metadata, ObjectIdStr


class Job(ModBaseModel):
    id: ObjectIdStr = Field(default_factory=ObjectIdStr, alias="_id")
    title: str
    company: Company
    location: tp.Optional[str] = "Remote"
    description: tp.Optional[str]
    date_posted: datetime.utcnow().date()
    is_delete: bool = False
    attachments: tp.List[Attachment] = []
    contact: tp.Union[Recruiter, ObjectId]
    metadata: tp.Optional[Metadata]
    expiration_date: datetime.utcnow().date()
