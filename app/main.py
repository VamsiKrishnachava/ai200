from fastapi import FastAPI

from app.routers.health import router as health_router
from app.routers.chat import router as chat_router
from app.exceptions.handlers import register_exception_handlers
from app.routers.db import router as db_router

app = FastAPI()
register_exception_handlers(app)


@app.get("/")
def home():
    return {"Message" : "Welcome to the FastAPI application!"}

app.include_router(health_router)
app.include_router(chat_router)
app.include_router(db_router)