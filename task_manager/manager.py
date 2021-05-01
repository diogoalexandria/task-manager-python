from fastapi import FastAPI

app = FastAPI()

TASKS = [
    {
        "id": "1",
        "title": "fazer compras",
        "description": "comprar leite e ovos",
        "status": "não finalizado",
    },
    {
        "id": "2",
        "title": "levar o cachorro para tosar",
        "description": "está muito peludo",
        "status": "não finalizado",
    },
    {
        "id": "3",
        "title": "lavar roupas",
        "description": "estão sujas",
        "status": "não finalizado",
    },
]

@app.get("/tasks")
def list():
    return TASKS