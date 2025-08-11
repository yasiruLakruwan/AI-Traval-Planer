from autogen_agentchat.agents import AssistantAgent
from config.settings import GEMINI_API_KEY
from autogen_ext.models.openai import OpenAIChatCompletionClient
from models.OpenAiModel import model_client

research_agent = AssistantAgent(
    name='research_agent',
    model_client=model_client,
    system_message= '''
                    You should do the research for the travaling places according to the user interests.
                    '''
)