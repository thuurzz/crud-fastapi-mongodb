from pydantic import BaseModel, Field, GetJsonSchemaHandler
from pydantic_core import CoreSchema
from typing import Any, Dict
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
    def __get_pydantic_json_schema__(
        cls, core_schema: CoreSchema, handler: GetJsonSchemaHandler
    ) -> Dict[str, Any]:
        json_schema = super().__get_pydantic_json_schema__(core_schema, handler)
        json_schema = handler.resolve_ref_schema(json_schema)
        json_schema.update(type="string")
        return json_schema

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
        json_schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "johndoe@example.com",
                "age": 30
            }
        }
