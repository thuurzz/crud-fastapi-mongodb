from ..db.database import get_collection
from bson import ObjectId
from ..models.models import PersonCreate, Person

def add_person(person_data: PersonCreate) -> Person:
    collection = get_collection("people")
    result = collection.insert_one(person_data.dict())
    return Person(**person_data.dict(), id=result.inserted_id)

def get_all_people() -> list:
    collection = get_collection("people")
    people = collection.find()
    return [Person(**person) for person in people]

def find_person(person_id: str) -> Person:
    collection = get_collection("people")
    person = collection.find_one({"_id": ObjectId(person_id)})
    if person:
        return Person(**person)
    return None

def update_person(person_id: str, person_data: PersonCreate) -> Person:
    collection = get_collection("people")
    collection.update_one({"_id": ObjectId(person_id)}, {"$set": person_data.dict()})
    return find_person(person_id)

def delete_person(person_id: str) -> bool:
    collection = get_collection("people")
    result = collection.delete_one({"_id": ObjectId(person_id)})
    return result.deleted_count > 0
