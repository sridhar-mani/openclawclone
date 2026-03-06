import lmstudio as lms
from dotenv import load_dotenv

load_dotenv()

def list_folder(path):
    import os
    try: 
        return os.listdir(path=path)
    except Exception as e:
        return str(e)
    
def read(file_path):
    try:
        with open(file_path,'r') as file:
            return file.read()
    except Exception as e:
        return str(e)

def write_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        return True
    except Exception as e:
        return str(e)

def append_file(file_path, content):
    try:
        with open(file_path, 'a') as file:
            file.write(content)
        return True
    except Exception as e:
        return str(e)