# 垂直应用主入口 - 闭环实现
from agent.agent import dict_agent, ex_agent, pron_agent, wb_agent, review_agent
from teams.robin_group import RobinGroup
from teams.select_group import SelectGroup
from teams.swarm import SwarmGroup

def run_vertical_app(word, user="Alice"):
    """
    闭环：查词义 -> 例句 -> 发音 -> 加入生词本 -> 生成复习计划
    支持三种团队模式
    """
    agents = [dict_agent, ex_agent, pron_agent, wb_agent, review_agent]
    robin_group = RobinGroup(agents)
    select_group = SelectGroup(agents)
    swarm_group = SwarmGroup(agents)

    # RobinGroup
    robin_result = robin_group.run(word, user)
    # SelectGroup（演示全流程）
    select_result = [
        select_group.run(word, "查词义", user),
        select_group.run(word, "例句", user),
        select_group.run(word, "发音", user),
        select_group.run(word, "生词本", user),
        select_group.run(word, "复习计划", user),
    ]
    # SwarmGroup
    swarm_result = swarm_group.run(word, user)
    return {
        "RobinGroup": robin_result,
        "SelectGroup": select_result,
        "SwarmGroup": swarm_result,
    }

if __name__ == "__main__":
    word = input("请输入你要学习的单词：").strip()
    result = run_vertical_app(word)
    print("RobinGroup结果：", result["RobinGroup"])
    print("SelectGroup结果：", result["SelectGroup"])
    print("SwarmGroup结果：", result["SwarmGroup"])