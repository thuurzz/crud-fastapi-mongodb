# tests/test_api.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() ==  {"status": "Ok"}

# Adicione mais testes para outros endpoints...
