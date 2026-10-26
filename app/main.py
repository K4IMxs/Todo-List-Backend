from fastapi import FastAPI

app = FastAPI(
    title = "Todo List API",
    description = " Back end sistema todo list",
    version = "0.0.1",
)

@app.get("/", tags=["Status"], summary="verificar se a api esta no ar")
def raiz() -> dict[str, str]:
    return{"mensagem": "todo-list online", "docutação": "/docs"}