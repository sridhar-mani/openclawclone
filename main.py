import os
import  lmstudio as lms
from ai.agent import main_agent_loop
from config import std_env

model = lms.llm(std_env.model_name)
    
convo_his = ''

while True:
    user_input = input('Ask agent to do a task:  ')
    if user_input.lower() in  ('exit','quit'):
        print("Goodbye!")
        break
    agent_res =  main_agent_loop(model,user_input, convo_his)


print(agent_res)