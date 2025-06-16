# [1, 11] 五个单Agent+Memory能力
from autogen import ConversableAgent, register_tool, Memory

@register_tool
def lookup(word: str) -> str:
    """查词义"""
    if not isinstance(word, str) or not word.strip():
        return "请输入有效单词"
    return f"{word} 的词义：苹果"

@register_tool
def pronounce(word: str) -> str:
    """发音"""
    return f"{word} 的发音：https://dict.youdao.com/dictvoice?audio={word}"

@register_tool
def example(word: str) -> str:
    """例句"""
    return f"{word} 的例句：I eat an apple every day."

@register_tool
def add_to_wordbook(word: str) -> str:
    """加入生词本"""
    return f"{word} 已加入生词本"

@register_tool
def review_plan(user: str) -> str:
    """生成复习计划"""
    return f"{user} 的今日复习单词：apple, banana"

class MemoryAgent(ConversableAgent):
    def __init__(self, name):
        super().__init__(name=name)
        self.memory = Memory()

    def memorize(self, word, meaning):
        self.memory[word] = meaning

    def recall(self, word):
        return self.memory.get(word, "未记忆")

dict_agent = ConversableAgent("DictAgent", tools=[lookup])
pron_agent = ConversableAgent("PronounceAgent", tools=[pronounce])
ex_agent   = ConversableAgent("ExampleAgent", tools=[example])
wb_agent   = ConversableAgent("WordBookAgent", tools=[add_to_wordbook])
review_agent = ConversableAgent("ReviewAgent", tools=[review_plan])
memory_agent = MemoryAgent("MemoryAgent")

if __name__ == "__main__":
    print(dict_agent.run_tool("apple"))
    print(pron_agent.run_tool("apple"))
    print(ex_agent.run_tool("apple"))
    print(wb_agent.run_tool("apple"))
    print(review_agent.run_tool("Alice"))
    memory_agent.memorize("apple", "苹果")
    print(memory_agent.recall("apple"))
    print(memory_agent.recall("banana"))