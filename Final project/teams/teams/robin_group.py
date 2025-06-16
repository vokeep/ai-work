# [2] RobinGroup团队，顺序分配
from agent.agent import dict_agent, ex_agent, pron_agent, wb_agent, review_agent

class RobinGroup:
    def __init__(self, agents):
        self.agents = agents

    def run(self, word, user="Alice"):
        results = []
        results.append(self.agents[0].run_tool(word)) # DictAgent
        results.append(self.agents[1].run_tool(word)) # ExampleAgent
        results.append(self.agents[2].run_tool(word)) # PronounceAgent
        results.append(self.agents[3].run_tool(word)) # WordBookAgent
        results.append(self.agents[4].run_tool(user)) # ReviewAgent
        return results

if __name__ == "__main__":
    group = RobinGroup([dict_agent, ex_agent, pron_agent, wb_agent, review_agent])
    print(group.run("apple"))