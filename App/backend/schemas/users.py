from typing import Optional
from click import password_option
from pydantic import BaseModel, EmailStr


# Properties required during user creation
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class ShowUser(BaseModel):
    username: str
    email: EmailStr
    is_active: bool
    is_superuser: bool

    class Config:
        """
        Informs pydantic to convert even non dict object to json
        """

        orm_mode = True
