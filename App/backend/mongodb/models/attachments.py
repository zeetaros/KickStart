from pydantic import Field

from models import ObjectIdStr, ModBaseModel


class Attachment(ModBaseModel):
    id: ObjectIdStr = Field(default_factory=ObjectIdStr, alias="_id")
    filename: str
    s3_filepath: str
    is_deleted: bool = False
