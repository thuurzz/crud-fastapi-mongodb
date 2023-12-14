from fastapi import FastAPI
from app.api.routes import router as api_router
from app.core.config import settings
from app.db.database import client

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Crud de pessoas"
)

@app.on_event("startup")
async def startup_event():
    # Código para inicialização, como estabelecer conexões de banco de dados
    print("Aplicação iniciada com sucesso.")
    pass

@app.on_event("shutdown")
async def shutdown_event():
    # Código para finalização, como fechar conexões de banco de dados
    print("Aplicação encerrada com sucesso.")
    client.close()

app.include_router(api_router)
