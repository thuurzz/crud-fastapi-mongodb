from fastapi import APIRouter, HTTPException, status
from typing import List
import logging
from ..models.models import Person, PersonCreate
from ..services.person_service import get_all_people, add_person, find_person, update_person, delete_person, delete_all_people

router = APIRouter()
logger = logging.getLogger(__name__)

# As rotas serão configuradas abaixo, mas o servidor MCP será criado no main.py
# a partir do aplicativo FastAPI completo


@router.get("/", operation_id="status_server")
async def status_server():
    """Verifica o status do sistema e retorna se está operacional."""
    return {"status": "Ok"}


@router.get("/customers", response_model=List[Person], operation_id="get_all")
async def get_all():
    """Retorna a lista de todas as clientes cadastradas no sistema."""
    try:
        people = get_all_people()
        logger.info("Fetching all people")
        return people
    except Exception as e:
        logger.error(f"Error fetching people: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/customers/{person_id}", response_model=Person, operation_id="get")
async def get(person_id: str):
    """Busca uma cliente específica pelo seu ID único."""
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


@router.post("/customers", response_model=Person, status_code=status.HTTP_201_CREATED, operation_id="create")
async def create(person: PersonCreate):
    """Cria um novo registro de cliente no sistema com os dados fornecidos."""
    try:
        new_person = add_person(person)
        logger.info(f"Person created with ID: {new_person.id}")
        return new_person
    except Exception as e:
        logger.error(f"Error creating person: {e}")
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/customers/{person_id}", response_model=Person, operation_id="update")
async def update(person_id: str, person: PersonCreate):
    """Atualiza os dados de uma cliente existente identificada pelo ID."""
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


@router.delete("/customers/{person_id}", status_code=status.HTTP_204_NO_CONTENT, operation_id="delete")
async def delete(person_id: str):
    """Remove uma cliente do sistema pelo seu ID."""
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


@router.delete("/customers", status_code=status.HTTP_204_NO_CONTENT, operation_id="delete_all")
async def delete_all():
    """Remove todas as clientes cadastradas no sistema."""
    try:
        deleted_count = delete_all_people()
        logger.info(f"Deleted {deleted_count} customers")
    except Exception as e:
        logger.error(f"Error deleting all customers: {e}")
        raise HTTPException(status_code=500, detail=str(e))


# Será configurado posteriormente pelo main.py
mcp_server = None

# Função para configurar o servidor MCP com as rotas get como ferramentas


def set_mcp_server(server):
    global mcp_server
    mcp_server = server
    # Registrar as ferramentas MCP
    if mcp_server:
        mcp_server.add_tool(
            status_server,
            name="status_server",
            description="Verifica o status do sistema e retorna se está operacional."
        )
        mcp_server.add_tool(
            get_all,
            name="get_all",
            description="Retorna a lista de todas as clientes cadastradas no sistema."
        )
        mcp_server.add_tool(
            get,
            name="get",
            description="Busca uma cliente específica pelo seu ID único."
        )
