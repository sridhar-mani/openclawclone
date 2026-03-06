from pydantic import BaseModel

class ModelResponse(BaseModel):
    message:str
    done: bool
    add_res: bool
    tool: str = ""
    tool_input: list = []

class SubModelResponse(BaseModel):
    result: str
    done: bool  