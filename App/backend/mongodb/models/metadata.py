import typing as tp
import datetime as dt
from pydantic import Field

from models import ObjectIdStr, ModBaseModel


class Metadata(ModBaseModel):
    id: ObjectIdStr = Field(default_factory=ObjectIdStr, alias="_id")
    created_timestamp: dt.datetime = Field(default_factory=dt.datetime.utcnow)
    created_user: str
    modified_timestamp: dt.datetime = Field(default_factory=dt.datetime.utcnow)
    modified_user: str
