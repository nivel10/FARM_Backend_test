from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    is_deleted: Optional[bool] = False
    created_at: Optional[int] = int(datetime.timestamp(datetime.now()))
    updated_at: Optional[int] = int(datetime.timestamp(datetime.now()))

class UserRegister(UserBase):
    password: str

class User(UserRegister):
    id: Optional[str] = None

class UserRegisterResponse(UserBase):
    id: Optional[str] = None

class UserLogin(BaseModel):
    email: str
    password: str
    remember_me: Optional[bool] = False