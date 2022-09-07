from datetime import datetime
from bson import ObjectId

from pydantic import Field

from mongodb.models.base_model import ModBaseModel, ObjectIdStr
from mongodb.models.companies import Company
from mongodb.models.attachments import Attachment
from mongodb.models.recruiters import Recruiter
from mongodb.models.metadata import Metadata


class Job(ModBaseModel):
    id: ObjectIdStr = Field(default_factory=ObjectIdStr, alias="_id")
    title: str
    company: Company
    locations: list[str] = ["Remote"]
    description: str | None
    date_posted: datetime = Field(default=datetime.utcnow().date())
    is_deleted: bool = False
    attachments: list[Attachment] = []
    contact: Recruiter | ObjectId
    metadata: Metadata | None
    expiration_date: datetime
