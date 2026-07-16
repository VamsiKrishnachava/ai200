from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.exceptions.chat import ChatNoMessageException

def register_exception_handlers(app:FastAPI):
    @app.exception_handler(ChatNoMessageException)
    async def chat_no_message_exception_handler(request, e:ChatNoMessageException):
        return JSONResponse(
            status_code=401, 
            content={"message": e.message}
        )