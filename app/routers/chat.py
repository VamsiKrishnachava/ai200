from fastapi import APIRouter

router = APIRouter(
    prefix = "/api/v1/chat",
    tags=['Chat']
)

@router.get("/")
def chat():
    return {"message": "Welcome to the Chat API!"}