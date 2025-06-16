from autogen import AssistantAgent, UserProxyAgent, SelectGroup

# 创建与保存时一致的代理
assistant = AssistantAgent(name="assistant", llm_config={"seed": 42})
user_proxy = UserProxyAgent(name="user_proxy", human_input_mode="NEVER")
group = SelectGroup(agents=[assistant])

# 加载状态
import json
with open("group_state.json", "r", encoding="utf-8") as f:
    state = json.load(f)
group.load_state(state)

# 继续对话
response = user_proxy.initiate_chat(group, message="请继续介绍你的能力。")
print(response)