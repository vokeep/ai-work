import asyncio

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.base import TaskResult
from autogen_agentchat.conditions import ExternalTermination, TextMentionTermination,SourceMatchTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_core import CancellationToken
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.agents import UserProxyAgent

from autogen_agentchat.teams import SelectorGroupChat

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



async def get_phone(phone:str)-> str:
    """"这是一个获取手机信息的工具，给定一个手机名字，会返回对应的信息"""
    return f"{phone}手机又128g内存,有5000毫安大电池，有骁龙Belite处理器"



# Define an AssistantAgent with the model, tool, system message, and reflection enabled.
# The system message instructs the agent via natural language.
b_agent = AssistantAgent(
    name="b_agent",
    model_client=model_client,
    tools=[get_phone],
    description="这是一个售前客服",
    system_message="""你是一个售前客服，你帮助用户完成手机销售前的产品介绍，推销
    """,
    reflect_on_tool_use=True,
    model_client_stream=True,  
)

after_agent = AssistantAgent(
    name="after_agent",
    model_client=model_client,
    system_message="""你是一个售后客服，用于解答用户中使用中所遇到的问题，完成手机的售后服务
    """,
    reflect_on_tool_use=True,
    model_client_stream=True, 
)

selector_prompt="""从以下agent中选择合适的agent执行任务

{roles}

当前对话的上下文:
{history}

Read the above conversation, then select an agent from {participants} to perform the next task.
Make sure the planner agent has assigned tasks before other agents start working.
Only select one agent.
"""

# Define a termination condition that stops the task if the critic approves.
termination1 = SourceMatchTermination(["b_agent","after_agent"])
termination2 = TextMentionTermination("停止")

termination=termination1 

# Create a team with the primary and critic agents.
team = SelectorGroupChat([b_agent, after_agent], termination_condition=termination,selector_prompt=selector_prompt,model_client=model_client)

# Run the agent and stream the messages to the console.
async def main() -> None:
    await Console(team.run_stream(task="小米15这个手机的怎么样/nothink"))
    # Close the connection to the model client.
    await model_client.close()


# NOTE: if running this inside a Python script you'll need to use asyncio.run(main()).
# await main()
asyncio.run(main())