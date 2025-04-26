from ..db.database import get_collection
from ..models.models import PersonCreate, Person
from bson import Binary
import uuid


def get_all_people() -> list:
    collection = get_collection("CUSTOMERS")
    people = collection.find()
    return [Person(**person) for person in people]


def add_person(person_data: PersonCreate) -> Person:
    collection = get_collection("CUSTOMERS")
    person_dict = person_data.model_dump()
    # Convertendo UUID para BSON Binary
    person_dict['id'] = Binary(uuid.uuid4().bytes, 4)
    collection.insert_one(person_dict)
    return Person(**person_dict)


def find_person(person_id: str) -> Person:
    collection = get_collection("CUSTOMERS")
    person = collection.find_one({"id": Binary(uuid.UUID(person_id).bytes, 4)})
    if person:
        return Person(**person)
    return None


def update_person(person_id: str, person_data: PersonCreate) -> Person:
    collection = get_collection("CUSTOMERS")
    collection.update_one(
        {"id": Binary(uuid.UUID(person_id).bytes, 4)},
        {"$set": person_data.model_dump(exclude={'id'})}
    )
    return find_person(person_id)


def delete_person(person_id: str) -> bool:
    collection = get_collection("CUSTOMERS")
    result = collection.delete_one(
        {"id": Binary(uuid.UUID(person_id).bytes, 4)})
    return result.deleted_count > 0


def delete_all_people() -> int:
    collection = get_collection("CUSTOMERS")
    result = collection.delete_many({})
    return result.deleted_count
