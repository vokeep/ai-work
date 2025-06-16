from autogen import AssistantAgent, UserProxyAgent, SelectGroup

# 创建多个专家代理
intro_agent = AssistantAgent(name="intro_agent", llm_config={"seed": 1})
analysis_agent = AssistantAgent(name="analysis_agent", llm_config={"seed": 2})
summary_agent = AssistantAgent(name="summary_agent", llm_config={"seed": 3})

# 用户代理
user_proxy = UserProxyAgent(name="user_proxy", human_input_mode="NEVER")

# SelectGroup 以团队方式分工
group = SelectGroup(
    agents=[intro_agent, analysis_agent, summary_agent],
    selector=SelectGroup.Selector.ALL
)

response = user_proxy.initiate_chat(
    group,
    message="请以‘人工智能在医疗中的应用’为主题，协作撰写一份报告，分为引言、应用分析和总结三部分。"
)

print(response)