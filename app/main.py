from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.routers import usuarios
from app.db.database import criar_tabelas

@asynccontextmanager
async def ciclo_de_vida(_app: FastAPI) -> AsyncIterator[None]:
    """Prepara o banco na subida da aplicação: cria as tabelas que faltam."""
    criar_tabelas()
    yield

app = FastAPI(
    title = "Todo List API",
    description = " Back end sistema todo list",
    version = "0.2.0",
    lifespan=ciclo_de_vida,
)

app.include_router(usuarios.router)

@app.get("/", tags=["Status"], summary="verificar se a api esta no ar")
def raiz() -> dict[str, str]:
    return{"mensagem": "todo-list online", "docutação": "/docs"}