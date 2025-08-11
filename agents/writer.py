from autogen_agentchat.agents import AssistantAgent
from models.OpenAiModel import model_client

writer_agent = AssistantAgent(
    name='writer_agent',
    description='You are a writer agent. Write a summary of the research details',
    model_client=model_client,
    system_message='You should write a breaf description of the foundings of yours about the traval places'
)