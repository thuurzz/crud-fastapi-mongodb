from fastapi import APIRouter, HTTPException, status
from typing import List
import logging
from ..models.models import Person, PersonCreate
from ..services.person_service import get_all_people, add_person, find_person, update_person, delete_person

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/")
async def status_server():
    return {"status": "Ok"}

@router.get("/people", response_model=List[Person])
async def read_people():
    try:
        people = get_all_people()
        logger.info("Fetching all people")
        return people
    except Exception as e:
        logger.error(f"Error fetching people: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/people", response_model=Person, status_code=status.HTTP_201_CREATED)
async def create_person(person: PersonCreate):
    try:
        new_person = add_person(person)
        logger.info(f"Person created with ID: {new_person.id}")
        return new_person
    except Exception as e:
        logger.error(f"Error creating person: {e}")
        raise HTTPException(status_code=400, detail=str(e))

# Exemplo de logs para as rotas PUT e DELETE

@router.put("/people/{person_id}", response_model=Person)
async def update_person_route(person_id: str, person: PersonCreate):
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

@router.delete("/people/{person_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_person_route(person_id: str):
    try:
        deleted = delete_person(person_id)
        if not deleted:
            logger.warning(f"Person with ID {person_id} not found for deletion")
            raise HTTPException(status_code=404, detail="Person not found")
        logger.info(f"Person with ID {person_id} deleted")
    except Exception as e:
        logger.error(f"Error deleting person with ID {person_id}: {e}")
        raise HTTPException(status_code=500, detail=str(e))
