import typing as tp
from datetime import datetime
from pydantic import Field

from models import ObjectIdStr, ModBaseModel


class Metadata(ModBaseModel):
    id: ObjectIdStr = Field(default_factory=ObjectIdStr, alias="_id")
    created_timestamp: datetime = Field(default_factory=datetime.utcnow)
    created_user: str
    modified_timestamp: datetime = Field(default_factory=datetime.utcnow)
    modified_user: str
