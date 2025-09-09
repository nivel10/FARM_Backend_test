from pydantic import BaseModel

class Db_collections(BaseModel):
    tasks: str

class Db_settings(BaseModel):
    url: str
    name: str
    # collections: Db_collections