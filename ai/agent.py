from .types import ModelResponse
from .tools.main import tool_list

def main_agent_loop(model,user_prompt, convo_his):
    Prompt=f"""
    Workspace Overview:
    data/
    workspace/

    Available Tools:
    - list(folder)
    - read(file)
    - write(file,content)
    - append(file,content)
    - subagent_call(file)

    Agent Goal:
    Help user analyze the data and achieve their goal.

    User Question:
    {user_prompt}
    """

    age_res = model.act(Prompt, [tool_list['list'],tool_list['read'],tool_list['append'],tool_list['write'],tool_list['subagent_call']])

    res = model.respond(age_res,response_format = ModelResponse)
    
    res = res.parsed


    res = ModelResponse(**res)

    print(res)


    if res.done:
        return res
    if res.tool:
        tool_res = tool_list[res.tool.split('(')[0]](*res.tool_input)
        convo_his+=f"""
    Agent:{res}
    Tool result:{tool_res}
"""
        return convo_his
