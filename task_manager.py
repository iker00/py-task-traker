import json
import os

from task import Task
from typing import Tuple


class TaskManager:
    def __init__(self, file_name="tasks.json"):
        self.file_name = file_name

        if not os.path.exists(self.file_name):
            self._initialize_file()

    def _initialize_file(self):
        initial_data = {"tasks": []}
        with open(self.file_name, 'w', encoding='UTF-8') as file:
            json.dump(initial_data, file, indent=4)

    def _load_tasks(self):
        try:
            with open(self.file_name, 'r', encoding='UTF-8') as file:
                data = json.load(file)
                # TODO Convertir el data en objetos de tipo Task para poder recorrerlos
                #  más facilmente y después poder serializarlos otra vez en json
                return data.get("tasks", [])
        except json.JSONDecodeError:
            print(f"Error reading {self.file_name}")
            exit(1)

    def _update_tasks(self, tasks: Tuple[Task, ...]):
        json_data = json.dumps({'tasks': [task.to_json() for task in tasks]})

        print(json_data)

        with open(self.file_name, 'w') as data:
            data.write(json_data)

    def add_task(self, description: str):
        if not description:
            raise ValueError("Description is required and should be a text")

        tasks = self._load_tasks()
        new_task_id = tasks[-1]['id'] + 1 if len(tasks) > 0 else 1

        task = Task(task_id=new_task_id, description=description)
        tasks.append(task)

        self._update_tasks(tasks)

        return new_task_id
