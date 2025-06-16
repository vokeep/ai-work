# [5] Swarm团队，并发协作
from concurrent.futures import ThreadPoolExecutor
from agent.agent import dict_agent, pron_agent, ex_agent, wb_agent, review_agent

class SwarmGroup:
    def __init__(self, agents):
        self.agents = agents

    def run(self, word, user="Alice"):
        # DictAgent, ExampleAgent, PronounceAgent, WordBookAgent, ReviewAgent并发
        def run_agent(idx):
            if idx == 4:
                return self.agents[idx].run_tool(user)
            else:
                return self.agents[idx].run_tool(word)
        with ThreadPoolExecutor() as executor:
            results = list(executor.map(run_agent, range(len(self.agents))))
        return results

if __name__ == "__main__":
    group = SwarmGroup([dict_agent, ex_agent, pron_agent, wb_agent, review_agent])
    print(group.run("apple"))