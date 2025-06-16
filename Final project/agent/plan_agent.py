# [2] PlanAgent任务分解
from autogen import PlanAndExecuteAgent

class VocabPlanAgent(PlanAndExecuteAgent):
    def plan(self, user_goal: str):
        import re
        # 支持从用户输入中抽取第一个英文单词
        word = "apple"
        match = re.search(r"\b([a-zA-Z]+)\b", user_goal)
        if match:
            word = match.group(1)
        steps = [
            ("DictAgent", word),
            ("ExampleAgent", word),
            ("PronounceAgent", word),
            ("WordBookAgent", word),
            ("ReviewAgent", "Alice")
        ]
        return steps

if __name__ == "__main__":
    agent = VocabPlanAgent()
    print(agent.plan("我要背单词banana"))