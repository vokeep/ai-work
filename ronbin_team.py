import asyncio

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.base import TaskResult
from autogen_agentchat.conditions import ExternalTermination, TextMentionTermination,SourceMatchTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_core import CancellationToken
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.agents import UserProxyAgent

# Define a model client. You can use other model client that implements
# the `ChatCompletionClient` interface.
model_client = OpenAIChatCompletionClient(
    model="Qwen/Qwen3-30B-A3B",
    api_key="sk-wvisouricjaqniuiwygffvcpvriyzbmvtrerdpimtdopjoza",
    base_url="https://api.siliconflow.cn/v1/",
    model_info={
        "vision": False,
        "function_calling": True,
        "json_output": False,
        "family": "qwen",
        "structured_output": True,
        "multiple_system_messages": True,
    },
)


# Define a simple function tool that the agent can use.
# For this example, we use a fake weather tool for demonstration purposes.
async def get_weather(city: str) -> str:
    """Get the weather for a given city."""
    return f"今天{city}是30℃，晴天"


# Define an AssistantAgent with the model, tool, system message, and reflection enabled.
# The system message instructs the agent via natural language.
weather_agent = AssistantAgent(
    name="weather_agent",
    model_client=model_client,
    tools=[get_weather],
    system_message="你是一个天气预报助手，可以通过Tool获取天气信息",
    reflect_on_tool_use=True,
    model_client_stream=True,  # Enable streaming tokens from the model client.
)

rednote_agent = AssistantAgent(
    name="rednote_agent",
    model_client=model_client,
    system_message="你是一个小红书网络达人，你擅长使用小红书的文本风格进行报告",
    reflect_on_tool_use=True,
    model_client_stream=True,  # Enable streaming tokens from the model client.
)

user_proxy=UserProxyAgent("user_proxy",input_func=input)

# Define a termination condition that stops the task if the critic approves.
text_termination = TextMentionTermination("停止",["user_proxy"])

# Create a team with the primary and critic agents.
team = RoundRobinGroupChat([weather_agent, rednote_agent], termination_condition=text_termination)

# Run the agent and stream the messages to the console.
async def main() -> None:
    await Console(team.run_stream(task="今天杭州是什么天气/nothink"))
    # Close the connection to the model client.
    await model_client.close()


# NOTE: if running this inside a Python script you'll need to use asyncio.run(main()).
# await main()
asyncio.run(main())