from fastapi import APIRouter
from fastapi.responses import Response
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat_service import ChatService

chatService = ChatService()

router = APIRouter(
    prefix = "/api/v1",
    tags=['Chat']
)

@router.post("/chat", response_model=ChatResponse)
def chat(chat_request: ChatRequest, response : Response):
    return chatService.process_message(chat_request)

@router.post("/upper", response_model=ChatResponse)
def upper(chat_request: ChatRequest):
    """This endpoint takes a message and returns the message in uppercase."""
    return chatService.upper_message(chat_request)