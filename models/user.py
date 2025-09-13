from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class User_base(BaseModel):
    first_name: str
    last_name: str
    email: str
    is_deleted: Optional[bool] = False
    created_at: Optional[int] = int(datetime.timestamp(datetime.now()))
    updated_at: Optional[int] = int(datetime.timestamp(datetime.now()))

class User_register(User_base):
    password: str

class User(User_register):
    id: Optional[str] = None

class User_register_response(User_base):
    id: Optional[str] = None

class User_login(BaseModel):
    email: str
    password: str
    remember_me: Optional[bool] = False