import os
import json
from task import Task

self.file_name = 'tasks.json'
DEFAULT_TASK_JSON = {'tasks': []}

def open_database():
    if not os.path.exists(self.file_name):
        with open(self.file_name, 'w', encoding='UTF-8') as f:
            json.dump(DEFAULT_TASK_JSON, f, indent=4)
        return DEFAULT_TASK_JSON

    try:
        with open(self.file_name, 'r', encoding='UTF-8') as f:
            content = f.read().strip()
            return json.loads(content) if content else DEFAULT_TASK_JSON
    except (json.JSONDecodeError, FileExistsError):
        return DEFAULT_TASK_JSON


def add_task(task: Task):
    with open(self.file_name, 'w') as database:
        database.write(task.to_json()  + "\n")
