import pytest
from app.schemas.chat import ChatRequest
from app.services.chat_service import ChatService


class FakeLLMClient:
    async def generate(self, messages, response_format=None):
        class Parsed:
            answer = "Fake AI response"

        class Message:
            refusal = None
            parsed = Parsed()

        class Choice:
            message = Message()

        class Response:
            choices = [Choice()]

        return Response()


@pytest.mark.asyncio
async def test_generate_with_fake_client():
    fake_client = FakeLLMClient()
    chat_service = ChatService(fake_client)
    chat_request = ChatRequest(message="Hello, AI!")

    response = await chat_service.generate(chat_request)

    assert response.response == "Fake AI response"

@pytest.mark.asyncio
async def test_generate_empty_message():
    fake_client = FakeLLMClient()
    chat_service = ChatService(fake_client)
    chat_request = ChatRequest(message="")

    with pytest.raises(Exception) as exc:
        await chat_service.generate(chat_request)

    assert str(exc.value) == "Provide a valid message to process."

@pytest.mark.asyncio
async def test_generate_whitespace_message():
    fake_client = FakeLLMClient()
    chat_service = ChatService(fake_client)
    chat_request = ChatRequest(message="   ")

    with pytest.raises(Exception) as exc:
        await chat_service.generate(chat_request)

    assert str(exc.value) == "Provide a valid message to process."