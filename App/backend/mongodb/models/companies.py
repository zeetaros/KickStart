from pydantic import Field

from mongodb.models import ObjectIdStr, ModBaseModel


class Company(ModBaseModel):
    id: ObjectIdStr = Field(default_factory=ObjectIdStr, alias="_id")
    company_number: str
    company_name: str
    sic: str
    homepage_url: str
    country: str
