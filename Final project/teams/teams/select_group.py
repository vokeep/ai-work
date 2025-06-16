# [4] SelectGroup团队，智能分配
from agent.agent import dict_agent, pron_agent, ex_agent, wb_agent, review_agent

class SelectGroup:
    def __init__(self, agents):
        self.agents = agents

    def run(self, word, task, user="Alice"):
        # 支持多种任务类型的智能分配
        if task == "查词义":
            return self.agents[0].run_tool(word)
        elif task == "发音":
            return self.agents[1].run_tool(word)
        elif task == "例句":
            return self.agents[2].run_tool(word)
        elif task == "生词本":
            return self.agents[3].run_tool(word)
        elif task == "复习计划":
            return self.agents[4].run_tool(user)
        else:
            return "未知任务类型"

if __name__ == "__main__":
    group = SelectGroup([dict_agent, pron_agent, ex_agent, wb_agent, review_agent])
    print(group.run("apple", "例句"))