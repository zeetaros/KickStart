from pydantic import BaseModel


class Company(BaseModel):
    company_number: str
    company_name: str
    sic: str
    homepage_url: str
