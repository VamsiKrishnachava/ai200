from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

class AIResponse(BaseModel):
    answer: str
    key_points: list[str]

class EmbedRequest(BaseModel):
    input_text: str

class EmbedResponse(BaseModel):
    embedding: list[float]