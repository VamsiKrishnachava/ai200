from app.schemas.chat import ChatRequest, ChatResponse
from app.core.settings import settings

class ChatService:
    def process_message(self, chat_request: ChatRequest) -> ChatResponse:
        # Here you can implement any logic to process the message
        return ChatResponse(response=f"Received message: {chat_request.message} and env has sam : {settings.sample} and gone : {settings.gone}")