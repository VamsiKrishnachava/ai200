from app.clients.embedding_model import EmbeddingModel
from app.services.chat_service import ChatService
from app.clients.azure_openai import AzureOpenAIClient
from app.services.embedd_service import EmbeddingService

llm_client = AzureOpenAIClient()
chat_service = ChatService(llm_client)

embedding_model = EmbeddingModel()
embedding_service = EmbeddingService(embedding_model)

def get_chat_service() -> ChatService:
    return chat_service

def get_embedding_service() -> EmbeddingService:
    return embedding_service