import asyncio
import json

from app.schemas.chat import ChatRequest, ChatResponse, AIResponse
from app.core.settings import settings
from app.exceptions.chat import ChatNoMessageException
from app.clients.azure_openai import AzureOpenAIClient
from app.prompts.v1 import SYSTEM_PROMPT
from app.tools.defnitions import CALCULATOR_TOOLS, CALCULATOR_TOOLS_RESPONSES
from openai import OpenAI

from app.tools.tool_functions import TOOL_FUNCTIONS

class ChatService:

    def __init__(self, llm_client):
        self.llm_client = llm_client

    def process_message(self, chat_request: ChatRequest) -> ChatResponse:
        # Here you can implement any logic to process the message
        if not chat_request.message or chat_request.message.strip() == "":
            raise ChatNoMessageException("Provide a valid message to process.")
        return ChatResponse(response=f"""Received message: {chat_request.message} 
                            and env has sam : {settings.sample} and gone : {settings.gone}""")
    

    def upper_message(self, chat_request: ChatRequest) -> ChatResponse:
        if not chat_request.message or chat_request.message.strip() == "":
            raise ChatNoMessageException("The provided message is empty.")
        return ChatResponse(response=chat_request.message.upper())

    async def generate(self, chat_request: ChatRequest) -> ChatResponse:
        if not chat_request.message or chat_request.message.strip() == "":
            raise ChatNoMessageException("Provide a valid message to process.")

        response =  await self.llm_client.generate(
            messages=[{"role": "system", 
                       "content": SYSTEM_PROMPT},
                      {"role": "user", 
                       "content": chat_request.message}],
            response_format=AIResponse
        )

        message = response.choices[0].message

        if message.refusal:
            raise ChatNoMessageException(f"The AI refused to answer: {message.refusal}")
        elif not message.parsed or not message.parsed.answer:
            raise ChatNoMessageException("The AI did not provide a valid response.")

        return ChatResponse(response=response.choices[0].message.parsed.answer if response.choices[0].message.parsed.answer else "")


    async def generate_with_tools(self, chat_request: ChatRequest) -> ChatResponse:
        if not chat_request.message or chat_request.message.strip() == "":
            raise ChatNoMessageException("Provide a valid message to process.")

        messages = [{"role": "system", 
                       "content": SYSTEM_PROMPT},
                      {"role": "user", 
                       "content": chat_request.message}]
        response =  await self.llm_client.generate_with_tools(
            messages=messages,
            tools=CALCULATOR_TOOLS
        )

        message = response.choices[0].message
        if message.refusal:
            raise ChatNoMessageException(f"The AI refused to answer: {message.refusal}")
        
        # Handle both text response and tool calls
        if message.content:
            return ChatResponse(response=message.content)
        elif message.tool_calls:
            messages.append(message)
            for toolCall in message.tool_calls:
                tool_name = toolCall.function.name
                if tool_name in TOOL_FUNCTIONS:
                    tool_function = TOOL_FUNCTIONS[tool_name]
                    arguments  = json.loads(toolCall.function.arguments)
                    response = tool_function(**arguments)
                    if asyncio.iscoroutine(response):
                        response = await response           
                    messages.append({"role": "tool", 
                                     "tool_call_id": toolCall.id, 
                                     "content": str(response)})
                else:
                    raise ChatNoMessageException(f"Tool {tool_name} is not defined.")
                
            response =  await self.llm_client.generate(
                        messages=messages,
                        response_format=AIResponse
                    )
            message = response.choices[0].message
            if message.refusal:
                raise ChatNoMessageException(f"The AI refused to answer: {message.refusal}")
            elif not message.parsed or not message.parsed.answer:
                raise ChatNoMessageException("The AI did not provide a valid response.")
    
            return ChatResponse(response=response.choices[0].message.parsed.answer if response.choices[0].message.parsed.answer else "")
    
        else:
            raise ChatNoMessageException("The AI did not provide a valid response.")



    async def generate_with_tools_latest(
        self,
        chat_request: ChatRequest,
    ) -> ChatResponse:
        
        if not chat_request.message or chat_request.message.strip() == "":
            raise ChatNoMessageException(
                "Provide a valid message to process."
            )

        response = await self.llm_client.generate_with_tools_latest(
            input=chat_request.message,
            tools=CALCULATOR_TOOLS_RESPONSES,
            instructions=SYSTEM_PROMPT
        )
        tool_outputs = []
        for item in response.output:
            if item.type != "function_call":
                continue
            if item.name in TOOL_FUNCTIONS:
                tool_function = TOOL_FUNCTIONS[item.name]
                arguments = json.loads(item.arguments)
                tool_response = tool_function(**arguments)
                if asyncio.iscoroutine(tool_response):
                    tool_response = await tool_response
                tool_outputs.append({
                    "type": "function_call_output",
                    "call_id": item.call_id,
                    "output": str(tool_response)
                })
            else:
                raise ChatNoMessageException(
                    f"Tool {item.name} is not defined."
                )
        if not tool_outputs:
            raise ChatNoMessageException(
                "The AI did not provide any tool outputs."
            )
        response = await self.llm_client.generate_with_tools_latest(
                    input=tool_outputs,
                    instructions=SYSTEM_PROMPT,
                    previous_response_id=response.id
                )
        for item in response.output:
            print("FINAL TYPE:", item.type)
            print("FINAL ITEM:", item)

        print("FINAL OUTPUT TEXT:", response.output_text)

        return ChatResponse(
            response=response.output_text or "No text output"
        )
