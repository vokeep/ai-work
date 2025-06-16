# [12] FastAPI Team接口，支持四团队
from fastapi import FastAPI, HTTPException
from teams.robin_group import RobinGroup
from teams.select_group import SelectGroup
from teams.swarm import SwarmGroup
from teams.graph_flow import VocabGraphFlow
from agent.agent import dict_agent, ex_agent, pron_agent, wb_agent, review_agent

app = FastAPI()

robin_group = RobinGroup([dict_agent, ex_agent, pron_agent, wb_agent, review_agent])
select_group = SelectGroup([dict_agent, pron_agent, ex_agent, wb_agent, review_agent])
swarm_group = SwarmGroup([dict_agent, ex_agent, pron_agent, wb_agent, review_agent])
graphflow_group = VocabGraphFlow()
teams = {
    "robin": robin_group,
    "select": select_group,
    "swarm": swarm_group,
    "graphflow": graphflow_group
}

@app.get("/team/{team_name}/{word}")
def get_team_result(team_name: str, word: str, task: str = "", user: str = "Alice"):
    team = teams.get(team_name)
    if not team:
        raise HTTPException(status_code=404, detail="团队不存在")
    if team_name == "select":
        return {"results": team.run(word, task, user)}
    return {"results": team.run(word, user)}

# 启动：uvicorn api.fastapi_team:app --reload