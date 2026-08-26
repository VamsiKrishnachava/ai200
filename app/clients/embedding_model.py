from app.clients.embedding_model_interface import EmbeddingModelInterface
from sentence_transformers import SentenceTransformer

class EmbeddingModel(EmbeddingModelInterface):
    def __init__(self):
        self.model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    def embed(self, input_text: str):
        return self.model.encode(input_text)