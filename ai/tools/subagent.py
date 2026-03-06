from config import std_env
from ..types import SubModelResponse
import lmstudio as lms

def subagent_call(data,task):
    sub_model = lms.llm(std_env.model_name)
    prompt = f"""
You are a senior consultant.

Data:
{data}

Task:
{task}


Instructions:
- Analyze the data carefully.
- Provide clear reasoning and answer.
- Use math and logical reasoning as needed.
- Respond concisely.
- Be Precise.
- No unnecessary details.
"""
    sub_res = sub_model.respond(prompt, response_format=SubModelResponse)

    parsed_res = SubModelResponse(**sub_res.parsed) if hasattr(sub_res, "parsed") else sub_res

    return parsed_res