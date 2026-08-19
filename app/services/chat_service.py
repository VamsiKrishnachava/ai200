from app.schemas.chat import ChatRequest, ChatResponse, AIResponse
from app.core.settings import settings
from app.exceptions.chat import ChatNoMessageException
from app.clients.azure_openai import AzureOpenAIClient
from openai import OpenAI

class ChatService:

    def __init__(self, llm_client):
        self.llm_client = llm_client

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

    async def generate(self, chat_request: ChatRequest) -> ChatResponse:
        if not chat_request.message or chat_request.message.strip() == "":
            raise ChatNoMessageException("Provide a valid message to process.")

        response =  await self.llm_client.generate(
            messages=[{"role": "user", "content": chat_request.message}],
            response_format=AIResponse
        )

        return ChatResponse(response=response.choices[0].message.parsed.key_points[0] if response.choices[0].message.parsed.answer)
