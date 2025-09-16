from pydantic import BaseModel

class DbCollections(BaseModel):
    tasks: str
    users: str

class DbSettings(BaseModel):
    url: str
    name: str
    # collections: Db_collections