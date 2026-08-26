from fastapi import APIRouter, Depends

from app.core.dependencies import get_embedding_service
from app.schemas.chat import AIResponse, EmbedRequest, EmbedResponse
from app.services.embedd_service import EmbeddingService


router = APIRouter(
    prefix = "/api/v1",
    tags=['Embeddings']
)

@router.post("/embedd", response_model=EmbedResponse)
def embed(request: EmbedRequest, service: EmbeddingService = Depends(get_embedding_service),):
    return service.embed(input_text=request.input_text)