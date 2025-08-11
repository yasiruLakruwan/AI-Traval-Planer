from autogen_agentchat.agents import AssistantAgent
from config.settings import GEMINI_API_KEY
from autogen_ext.models.openai import OpenAIChatCompletionClient
from models.OpenAiModel import model_client

planer_agent = AssistantAgent(
    name='planeragent',
    description='A traval planner agent that helps users to plan their travals',
    model_client=model_client,
    system_message='You are a travel planner agent. Your task is to help users to plan their trips providing information about traveling places around the world'
)