from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId
from datetime import datetime

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid object id")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

class PersonBase(BaseModel):
    name: str
    email: Optional[str] = None
    age: Optional[int] = None

class PersonCreate(PersonBase):
    pass

class PersonUpdate(PersonBase):
    name: Optional[str] = None

class Person(PersonBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "johndoe@example.com",
                "age": 30
            }
        }
