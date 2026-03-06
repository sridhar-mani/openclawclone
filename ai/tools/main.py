from .subagent import subagent_call
from .filesystem import append_file, list_folder, read, write_file

tool_list={
    "list":list_folder,
    "read": read,
    "write" : write_file,
    "append": append_file,
    "subagent_call": subagent_call
}