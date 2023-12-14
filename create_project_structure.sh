#!/bin/bash

# Criando os subdiretórios
mkdir -p app/api
mkdir -p app/core
mkdir -p app/models
mkdir -p app/services
mkdir -p app/db
mkdir tests
mkdir utils

# Criando arquivos __init__.py para tornar os diretórios pacotes Python
touch app/api/__init__.py
touch app/core/__init__.py
touch app/models/__init__.py
touch app/services/__init__.py
touch app/db/__init__.py
touch tests/__init__.py

# Criando arquivos principais
touch main.py
touch app/api/routes.py
touch app/core/config.py
touch app/models/models.py
touch app/services/crud_service.py
touch app/db/database.py
touch tests/test_api.py
touch tests/test_services.py
touch utils/utils.py

# Arquivos adicionais
touch requirements.txt
touch README.md

echo "Estrutura de pastas criada com sucesso!"
