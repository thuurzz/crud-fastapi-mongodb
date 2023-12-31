from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.routes import router as api_router
from app.core.config import settings
from app.db.database import client


@asynccontextmanager
async def lifespan(app: FastAPI):
    # faça algo antes de iniciar o servidor
    pass

    yield
    # faça algo antes de finalizar o servidor
    client.close()

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Crud de pessoas",
    lifespan=lifespan
)

app.include_router(api_router)
