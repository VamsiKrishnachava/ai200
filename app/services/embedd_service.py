from app.clients.embedding_model_interface import EmbeddingModelInterface
from app.schemas.chat import AIResponse, EmbedResponse
from app.schemas.chat import AIResponse

class EmbeddingService:
    def __init__(self, embedding_model: EmbeddingModelInterface):
        self.embedding_model = embedding_model

    def embed(self, input_text: str):
        response = self.embedding_model.embed(input_text)
        return EmbedResponse(embedding=response)