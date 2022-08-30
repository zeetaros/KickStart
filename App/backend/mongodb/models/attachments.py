from pydantic import BaseModel, Field

from models import ObjectIdStr


class Attachment(BaseModel):
    id: str = Field(default_factory=lambda: str(ObjectIdStr))
    filename: str
    s3_filepath: str
    is_delete: bool = False
