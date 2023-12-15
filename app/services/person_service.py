from ..db.database import get_collection
from ..models.models import PersonCreate, Person
from bson import Binary
import uuid

def get_all_people() -> list:
    collection = get_collection("people")
    people = collection.find()
    return [Person(**person) for person in people]

def add_person(person_data: PersonCreate) -> Person:
    collection = get_collection("people")
    person_dict = person_data.model_dump()
    person_dict['id'] = Binary(uuid.uuid4().bytes, 4)  # Convertendo UUID para BSON Binary
    collection.insert_one(person_dict)
    return Person(**person_dict)

def find_person(person_id: str) -> Person:
    collection = get_collection("people")
    person = collection.find_one({"id": Binary(uuid.UUID(person_id).bytes, 4)})
    if person:
        return Person(**person)
    return None

def update_person(person_id: str, person_data: PersonCreate) -> Person:
    collection = get_collection("people")
    collection.update_one(
        {"id": Binary(uuid.UUID(person_id).bytes, 4)}, 
        {"$set": person_data.model_dump(exclude={'id'})}
    )
    return find_person(person_id)

def delete_person(person_id: str) -> bool:
    collection = get_collection("people")
    result = collection.delete_one({"id": Binary(uuid.UUID(person_id).bytes, 4)})
    return result.deleted_count > 0
