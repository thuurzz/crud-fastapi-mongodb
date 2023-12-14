
# Projeto CRUD de Pessoas

Este projeto implementa um sistema CRUD (Create, Read, Update, Delete) para um registro de pessoas. Desenvolvido com FastAPI e MongoDB, oferece uma API robusta e eficiente para gerenciamento de dados de pessoas.

## Funcionalidades

- **Cadastrar Pessoa**: Adicionar novas pessoas ao sistema.
- **Listar Pessoas**: Visualizar todas as pessoas cadastradas.
- **Buscar Pessoa**: Obter detalhes de uma pessoa específica.
- **Atualizar Pessoa**: Modificar informações de uma pessoa.
- **Remover Pessoa**: Deletar o registro de uma pessoa do sistema.

## Tecnologias Utilizadas

- **FastAPI**: Framework web moderno e rápido para construção de APIs com Python 3.7+.
- **MongoDB**: Banco de dados NoSQL, orientado a documentos, que oferece alta performance e escalabilidade.

## Instalação

Para executar este projeto localmente, siga estas etapas:

1. Clone o repositório:
   ```bash
   git clone https://seu-repositorio/projeto-crud-pessoas.git
   cd projeto-crud-pessoas
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure as variáveis de ambiente:
   - Defina a string de conexão com o MongoDB em `app/core/config.py`.

4. Execute a aplicação:
   ```bash
   uvicorn main:app --reload
   ```

A API estará disponível em `http://localhost:8000`.

## Documentação da API

A documentação interativa da API, gerada pelo Swagger, pode ser acessada em `http://localhost:8000/docs`.

## Testes

Para executar os testes, utilize o seguinte comando:

```bash
pytest
```

## Contribuições

Contribuições são bem-vindas! Por favor, leia o `CONTRIBUTING.md` para saber como contribuir para o projeto.

## Licença

Este projeto está sob a licença XYZ. Veja o arquivo `LICENSE` para mais detalhes.

---

Desenvolvido por [Seu Nome](link-para-seu-perfil).
