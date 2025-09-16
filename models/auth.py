from pydantic import BaseModel

class BearerToken(BaseModel):
    token: str

class UserPassword(BaseModel):
    user_password: str