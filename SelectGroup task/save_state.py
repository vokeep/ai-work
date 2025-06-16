from autogen import AssistantAgent, UserProxyAgent, SelectGroup

assistant = AssistantAgent(name="assistant", llm_config={"seed": 42})
user_proxy = UserProxyAgent(name="user_proxy", human_input_mode="NEVER")
group = SelectGroup(agents=[assistant])

# 先进行一轮对话
response = user_proxy.initiate_chat(group, message="你好，介绍一下你自己。")
print(response)

# 保存对话状态到文件
state = group.get_state()
import json
with open("group_state.json", "w", encoding="utf-8") as f:
    json.dump(state, f, ensure_ascii=False, indent=2)
print("状态已保存。")