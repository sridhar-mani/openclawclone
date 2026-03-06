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

    res = model.respond(Prompt, response_format = ModelResponse)

    
    res = res.parsed


    res = ModelResponse(**res)

    print(res)

    if len(res.tool)>0 and len(res.tool)>0:
        tool_res = tool_list[res.tool.split('(')[0]](*res.tool_input)

    if res.done:
        return res
    if tool_res:
        convo_his+=f"""
    Agent:{res}
    Tool result:{tool_res}
"""
