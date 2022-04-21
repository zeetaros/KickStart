from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt

from core.config import settings


def create_access_token(data:dict, expires_delta:Optional[timedelta]=None):
     """
     Args:
         data (dict): a data dictionary with a subject which ideally is an email or username that can uniquely identify each record in the table.
         expires_delta (Optional[timedelta], optional): expiry time after which the access token will become invalid. Defaults to None as function argument, 
                                                        but the auto-expire is control by the pre-set value in settings.

     Returns:
         _type_: a encoded token, which has made use of secret key and algorthms to encode the data dictionary.
     """
     to_encode = data.copy()
     if expires_delta:
          expire = datetime.utcnow() + expires_delta
     else:
          expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
     to_encode.update({"exp": expire})
     encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
     return encoded_jwt 