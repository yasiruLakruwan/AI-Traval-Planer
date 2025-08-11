from autogen_agentchat.conditions import TextMentionTermination
import json

text_mention_termination = TextMentionTermination(text='Terminate')

def save_state(agent,filename):
    state = agent.save_state()
    with open(filename,'w') as f:
        json.dump(state , f)

def load_state(agent,filename):
    with open(filename,'r') as f:
        state = json.load(f)
    agent.load_state(state)

