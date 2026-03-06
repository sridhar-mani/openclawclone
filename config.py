from dotenv import load_dotenv 
import os

load_dotenv()

class std_env:
    model_name = os.getenv("MODEL_NAME")

    