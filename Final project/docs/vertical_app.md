# 垂直应用需求分析与设计

## 需求分析
本应用面向英语学习者，帮助用户高效、智能地背单词。用户可查词义、发音、例句，管理生词本，自动生成复习计划，并可随时恢复进度。应用支持多Agent协作及多种团队模式的对比评测，提升学习体验和效率。

## 所需功能分析
- 单词查询（词义/发音/例句）
- 生词本管理（添加/查看/复习）
- 复习计划自动生成与执行
- 任务与学习进度保存/恢复
- 多团队协作与对比评测

## Agent设计
- DictAgent：负责词义查询
- PronounceAgent：负责发音
- ExampleAgent：负责例句
- WordBookAgent：负责生词本管理
- ReviewAgent：负责学习计划
- MemoryAgent：负责记忆功能

## Team设计
- RobinGroup：轮流分配任务，提升效率
- SelectGroup：根据任务类型智能选择Agent
- SwarmGroup：并行协作，提升响应速度
- GraphFlowGroup：图流式高级任务流控制
团队通过协作，实现单词学习、复习和记忆的闭环。