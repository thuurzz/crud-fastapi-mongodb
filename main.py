from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api.routes import router as api_router, set_mcp_server
from app.core.config import settings
from app.db.database import client
from fastmcp import FastMCP

# ___________________________ FASTAPI ___________________________


@asynccontextmanager
async def lifespan(app: FastAPI):
    # faça algo antes de iniciar o servidor
    pass

    yield
    # faça algo antes de finalizar o servidor
    client.close()

# Manter o FastAPI para compatibilidade com endpoints existentes
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Cadastro de clientes",
    lifespan=lifespan,
)
app.include_router(api_router)

# ___________________________ MCP ___________________________

# Criar servidor MCP a partir do aplicativo FastAPI existente
mcp_server = FastMCP.from_fastapi(
    app,
    name="Cadastro de clientes"
)

# Configurar o servidor MCP no módulo de rotas para registrar as ferramentas
set_mcp_server(mcp_server)

# ____________________________ RODAR O SERVIDOR ___________________________
if __name__ == "__main__":
    import uvicorn
    import threading

    # Iniciar o servidor FastAPI em uma thread separada
    def start_fastapi():
        print(
            f"⚡ FastAPI server starting on http://{settings.HOST}:{settings.PORT}")
        print(f"📚 API Documentation available at:")
        print(f"   - Swagger UI: http://{settings.HOST}:{settings.PORT}/docs")
        print(f"   - ReDoc: http://{settings.HOST}:{settings.PORT}/redoc")
        uvicorn.run(
            app=app,
            host=settings.HOST,
            port=int(settings.PORT),
            log_level="info",
        )

    # print("🚀 Starting CRUD application servers...")
    # fastapi_thread = threading.Thread(target=start_fastapi)
    # fastapi_thread.daemon = True
    # fastapi_thread.start()

    # Iniciar o servidor MCP usando o aplicativo FastAPI existente
    print("🔌 Starting MCP server with stdio transport")
    mcp_server.run(transport="stdio")
