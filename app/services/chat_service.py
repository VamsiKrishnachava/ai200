from app.schemas.chat import ChatRequest, ChatResponse
from app.core.settings import settings
from app.exceptions.chat import ChatNoMessageException

class ChatService:
    def process_message(self, chat_request: ChatRequest) -> ChatResponse:
        # Here you can implement any logic to process the message
        if not chat_request.message or chat_request.message.strip() == "":
            raise ChatNoMessageException("Provide a valid message to process.")
        return ChatResponse(response=f"""Received message: {chat_request.message} 
                            and env has sam : {settings.sample} and gone : {settings.gone}""")
    

    def upper_message(self, chat_request: ChatRequest) -> ChatResponse:
        if not chat_request.message or chat_request.message.strip() == "":
            raise ChatNoMessageException("The provided message is empty.")
        return ChatResponse(response=chat_request.message.upper())