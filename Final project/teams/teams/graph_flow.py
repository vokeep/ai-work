# [8] GraphFlow团队，官方推荐接口
from autogen import GraphFlow, Node, Edge
from agent.agent import dict_agent, ex_agent, pron_agent, wb_agent, review_agent

class VocabGraphFlow(GraphFlow):
    def __init__(self):
        nodes = [
            Node("dict", dict_agent),
            Node("example", ex_agent),
            Node("pronounce", pron_agent),
            Node("wordbook", wb_agent),
            Node("review", review_agent)
        ]
        edges = [
            Edge("dict", "example"),
            Edge("example", "pronounce"),
            Edge("pronounce", "wordbook"),
            Edge("wordbook", "review")
        ]
        super().__init__(nodes, edges)

    def run(self, word, user="Alice"):
        # 只传递主单词和用户，GraphFlow自动依赖执行
        return self.execute((word, user))

if __name__ == "__main__":
    graph = VocabGraphFlow()
    print(graph.run("apple"))