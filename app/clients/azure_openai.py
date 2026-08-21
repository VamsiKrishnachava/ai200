import asyncio

try:
    from openai import AsyncOpenAI
except ImportError:
    from openai import OpenAI

    class AsyncOpenAI(OpenAI):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

from app.core.settings import settings


class AzureOpenAIClient:

    def __init__(self):
        self.client = AsyncOpenAI(
            api_key=settings.AZURE_OPENAI_API_KEY,
            base_url=f"{settings.AZURE_OPENAI_ENDPOINT}/openai/v1/",
        )

    async def generate(self, messages, response_format):
        parse_fn = self.client.beta.chat.completions.parse
        request_kwargs = {
            "model": settings.AZURE_OPENAI_DEPLOYMENT,
            "messages": messages,
            "response_format": response_format,
        }

        if asyncio.iscoroutinefunction(parse_fn):
            return await parse_fn(**request_kwargs)

        return await asyncio.to_thread(parse_fn, **request_kwargs)