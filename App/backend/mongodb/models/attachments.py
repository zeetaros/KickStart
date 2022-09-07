from pydantic import Field

from mongodb.models import ObjectIdStr, ModBaseModel


class Attachment(ModBaseModel):
    id: ObjectIdStr = Field(default_factory=ObjectIdStr, alias="_id")
    filename: str
    s3_filepath: str
    is_deleted: bool = False
