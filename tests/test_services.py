# tests/test_services.py
from app.services.person_service import add_person
from app.models.models import PersonCreate


def test_add_person():
    person_data = PersonCreate(name="John Doe", age=30)
    result = add_person(person_data)
    assert result.name == "John Doe"
    assert result.age == 30
# Adicione mais testes unitários para suas funções de serviços...
