from autogen import AssistantAgent, UserProxyAgent, SelectGroup

# 1. 创建代理
assistant1 = AssistantAgent(name="assistant1", llm_config={"seed": 42})
assistant2 = AssistantAgent(name="assistant2", llm_config={"seed": 43})
user_proxy = UserProxyAgent(name="user_proxy", human_input_mode="NEVER")

# 2. 创建 SelectGroup
group = SelectGroup(
    agents=[assistant1, assistant2],
    selector=SelectGroup.Selector.ALL,   # 这里可选 ALL/ANY/ONE, 根据任务可调整
)

# 3. 发送消息
response = user_proxy.initiate_chat(
    group,
    message="帮我搜索一下Python的应用场景，并给出总结。",
)

print(response)