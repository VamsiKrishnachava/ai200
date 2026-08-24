from fastapi import APIRouter, Depends
from fastapi.responses import Response
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat_service import ChatService
from app.core.dependencies import get_chat_service


router = APIRouter(
    prefix = "/api/v1",
    tags=['Chat']
)

@router.post("/chat", response_model=ChatResponse)
async def chat(chat_request: ChatRequest,
               service: ChatService = Depends(get_chat_service),):
    return await service.generate(chat_request)

@router.post("/upper", response_model=ChatResponse)
def upper(chat_request: ChatRequest, service: ChatService = Depends(get_chat_service)):
    """This endpoint takes a message and returns the message in uppercase."""
    return service.upper_message(chat_request)

@router.post("/tool", response_model=ChatResponse)
async def tool(chat_request: ChatRequest,
               service: ChatService = Depends(get_chat_service),
               latest: bool = False):
    if latest:
        return await service.generate_with_tools_latest(chat_request)
    return await service.generate_with_tools(chat_request)