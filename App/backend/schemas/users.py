from typing import Optional
from click import password_option
from pydantic import BaseModel, EmailStr


# Properties required during user creation
class UserCreate(BaseModel):
     username: str
     email: EmailStr
     password: str

