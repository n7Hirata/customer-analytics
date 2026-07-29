from pydantic import BaseModel
from datetime import datetime


class CreateClient(BaseModel):
    name: str
    email: str

class UpdateClient(BaseModel):
    name: str | None = None
    email: str | None = None

class ResponseClient(BaseModel):
    id: int
    name: str
    email: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True