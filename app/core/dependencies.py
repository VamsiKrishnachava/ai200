from app.services.chat_service import ChatService
from app.clients.azure_openai import AzureOpenAIClient

llm_client = AzureOpenAIClient()
chat_service = ChatService(llm_client)

def get_chat_service() -> ChatService:
    return chat_service