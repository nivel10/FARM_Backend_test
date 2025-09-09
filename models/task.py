from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Task (BaseModel):
    id: Optional[str] = None
    title: str
    description: Optional[str] = None
    completed: Optional[bool] = False
    is_deleted: Optional[bool] = False
    created_at: int = int(datetime.timestamp(datetime.now()))
    updated_at: int = int(datetime.timestamp(datetime.now()))