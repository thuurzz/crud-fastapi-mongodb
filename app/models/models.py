from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
import uuid

class PersonBase(BaseModel):
    name: str
    email: Optional[str] = None
    age: Optional[int] = None

class PersonCreate(PersonBase):
    pass

class PersonUpdate(PersonBase):
    name: Optional[str] = None

class Person(PersonBase):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, alias="id")
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_encoders = {
            uuid.UUID: lambda v: str(v),  # Convert UUID to string for JSON responses
            datetime: lambda v: v.isoformat()  # Convert datetime to ISO format string
        }
