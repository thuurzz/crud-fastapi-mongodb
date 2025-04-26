from pymongo import MongoClient
from ..core.config import settings

# Criação do cliente MongoDB
client = MongoClient(settings.DATABASE_URL)

# Selecionando o banco de dados
db = client['DB_CUSTOMERS']

# Função para obter uma coleção específica
def get_collection(collection_name: str):
    return db[collection_name]
