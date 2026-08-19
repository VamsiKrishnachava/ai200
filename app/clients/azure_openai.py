from openai import AsyncOpenAI

from app.core.settings import settings


class AzureOpenAIClient:

    def __init__(self):
        self.client = AsyncOpenAI(
            api_key=settings.AZURE_OPENAI_API_KEY,
            base_url=f"{settings.AZURE_OPENAI_ENDPOINT}/openai/v1/",
        )

    async def generate(self, messages, response_format):
        return await self.client.beta.chat.completions.parse(
            model=settings.AZURE_OPENAI_DEPLOYMENT,
            messages=messages,
            response_format=response_format,
        )