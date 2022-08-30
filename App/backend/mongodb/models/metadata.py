from lib2to3.pytree import Base
import typing
import datetime as dt
from pydantic import BaseModel, Field

from models import ObjectIdStr


class Metadata(BaseModel):
    id: ObjectIdStr = Field(default_factory=ObjectIdStr, alias="_id")
    created_timestamp: dt.datetime = Field(default_factory=dt.datetime.utcnow)
    created_user: str
    modified_timestamp: dt.datetime = Field(default_factory=dt.datetime.utcnow)
    modified_user: str
