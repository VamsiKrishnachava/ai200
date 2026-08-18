from openai import OpenAI
from app.core.settings import settings

class AzureOpenAIClient:
    def __init__(self):
        self.client = OpenAI(
            base_url=f'{settings.AZURE_OPENAI_ENDPOINT}/openai/v1/',
            api_key=settings.AZURE_OPENAI_API_KEY,
        )

    async def generate(self, messages):
        return self.client.chat.completions.create(
            model=settings.AZURE_OPENAI_DEPLOYMENT,
            messages=messages,
        )