from fastapi import APIRouter, HTTPException, status
from typing import List
import logging
from ..models.models import Person, PersonCreate
from ..services.person_service import get_all_people, add_person, find_person, update_person, delete_person, delete_all_people

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/")
async def status_server():
    return {"status": "Ok"}


@router.get("/customers", response_model=List[Person])
async def get_all():
    try:
        people = get_all_people()
        logger.info("Fetching all people")
        return people
    except Exception as e:
        logger.error(f"Error fetching people: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/customers/{person_id}", response_model=Person)
async def get(person_id: str):
    try:
        person = find_person(person_id)
        if person is None:
            logger.warning(f"Person with ID {person_id} not found")
            raise HTTPException(status_code=404, detail="Person not found")
        logger.info(f"Person with ID {person_id} fetched")
        return person
    except Exception as e:
        logger.error(f"Error fetching person with ID {person_id}: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/customers", response_model=Person, status_code=status.HTTP_201_CREATED)
async def create(person: PersonCreate):
    try:
        new_person = add_person(person)
        logger.info(f"Person created with ID: {new_person.id}")
        return new_person
    except Exception as e:
        logger.error(f"Error creating person: {e}")
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/customers/{person_id}", response_model=Person)
async def update(person_id: str, person: PersonCreate):
    try:
        updated_person = update_person(person_id, person)
        if updated_person is None:
            logger.warning(f"Person with ID {person_id} not found for update")
            raise HTTPException(status_code=404, detail="Person not found")
        logger.info(f"Person with ID {person_id} updated")
        return updated_person
    except Exception as e:
        logger.error(f"Error updating person with ID {person_id}: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/customers/{person_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(person_id: str):
    try:
        deleted = delete_person(person_id)
        if not deleted:
            logger.warning(
                f"Person with ID {person_id} not found for deletion")
            raise HTTPException(status_code=404, detail="Person not found")
        logger.info(f"Person with ID {person_id} deleted")
    except Exception as e:
        logger.error(f"Error deleting person with ID {person_id}: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/customers", status_code=status.HTTP_204_NO_CONTENT)
async def delete_all():
    try:
        deleted_count = delete_all_people()
        logger.info(f"Deleted {deleted_count} customers")
    except Exception as e:
        logger.error(f"Error deleting all customers: {e}")
        raise HTTPException(status_code=500, detail=str(e))
