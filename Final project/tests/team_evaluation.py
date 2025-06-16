# 团队评测脚本，自动统计多团队表现
import time
from app.vertical_app import run_vertical_app

def evaluate_teams(words, user="Alice"):
    stats = {"RobinGroup": [], "SelectGroup": [], "SwarmGroup": []}
    for word in words:
        print(f"\n[测试单词: {word}]")
        start = time.time()
        result = run_vertical_app(word, user)
        end = time.time()
        elapsed = end - start
        for team in stats:
            stats[team].append(elapsed)  # 这里为简单统计，实际可细分各团队耗时
        print(result)
    # 输出平均耗时
    for team in stats:
        avg = sum(stats[team]) / len(stats[team])
        print(f"{team} 平均响应时间: {avg:.2f}s")
    return stats

if __name__ == "__main__":
    test_words = ["apple", "banana", "orange"]
    evaluate_teams(test_words)