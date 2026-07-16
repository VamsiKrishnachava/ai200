from fastapi import APIRouter

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat_service import ChatService

chatService = ChatService()

router = APIRouter(
    prefix = "/api/v1/chat",
    tags=['Chat']
)

@router.post("/", response_model=ChatResponse)
def chat(chat_request: ChatRequest):
    return chatService.process_message(chat_request)