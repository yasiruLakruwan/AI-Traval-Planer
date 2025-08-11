from autogen_agentchat.agents import AssistantAgent
from config.settings import GEMINI_API_KEY, MODEL
from autogen_ext.models.openai import OpenAIChatCompletionClient

model_client = OpenAIChatCompletionClient(model=MODEL,api_key=GEMINI_API_KEY)
