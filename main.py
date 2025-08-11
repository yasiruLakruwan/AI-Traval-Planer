from autogen_agentchat.messages import TextMessage
from teams.travel_team import team
import asyncio

async def main():
    task = TextMessage(content='Plan a trip to paris for 5 days',source='user'),
    result = await team.run_stream(task=task)

    for message in result.messages:
        print(f"{message.source} : {message.content}")

if __name__=="__main__":
    asyncio.run(main())
