from autogen_agentchat.teams import RoundRobinGroupChat
from agents.planner import planer_agent
from agents.researcher import research_agent
from agents.writer import writer_agent
from autogen_agentchat.conditions import TextMentionTermination

termination_condition = TextMentionTermination(text="Terminate")

team = RoundRobinGroupChat(
    participants=[planer_agent,research_agent,writer_agent],
    description='A team of agents that help users to plan their trips by providing informations' \
    'itineraries, and traval trips.',
    termination_condition=termination_condition
)