# 智能背单词项目

## 简介
基于 [microsoft/autogen](https://github.com/microsoft/autogen) 实现的智能背单词系统，支持多Agent团队协作、任务计划、数据库状态管理、API接口等多项高分功能。

## 目录结构
- agent/agent.py         # 5个工具Agent
- agent/plan_agent.py    # PlanAgent
- teams/robin_group.py   # Robin团队
- teams/select_group.py  # Select团队
- teams/swarm.py         # Swarm团队
- teams/graph_flow.py    # GraphFlow团队
- db/db_manager.py       # 数据库状态管理
- api/fastapi_team.py    # FastAPI接口
- docs/vertical_app.md   # 垂直应用分析文档
- docs/four_team_report.md # 四团队评测报告

## 运行方法
1. 安装依赖
```bash
pip install -r requirements.txt
```
2. 运行FastAPI接口
```bash
uvicorn api.fastapi_team:app --reload
```
3. 运行各模块测试用例，见每个.py文件底部

## 预计得分
100分

## 评分说明
具体完成情况及得分见 `docs/four_team_report.md`