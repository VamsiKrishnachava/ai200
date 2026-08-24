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
        result = self.client.beta.chat.completions.parse(
            model=settings.AZURE_OPENAI_DEPLOYMENT,
            messages=messages,
            response_format=response_format,
        )
        
        # Check if result is a coroutine and await it if necessary
        if asyncio.iscoroutine(result):
            return await result
        
        return result


    async def generate_with_tools(self, messages, tools):
        result = self.client.responses.create(
            model=settings.AZURE_OPENAI_DEPLOYMENT,
            messages=messages,
            tools=tools,
        )
        
        # Check if result is a coroutine and await it if necessary
        if asyncio.iscoroutine(result):
            return await result
        
        return result

    async def generate_with_tools_latest(self, input, instructions=None, tools=None, previous_response_id=None):
            result = self.client.responses.create(
                model=settings.AZURE_OPENAI_DEPLOYMENT,
                input=input,
                tools=tools,
                instructions=instructions,
                previous_response_id=previous_response_id
            )
            
            # Check if result is a coroutine and await it if necessary
            if asyncio.iscoroutine(result):
                return await result
            
            return result