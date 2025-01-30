import json
import os
from task import Task


class TaskManager:
    def __init__(self, file_name="tasks.json"):
        self.file_name = file_name

        if not os.path.exists(self.file_name):
            self._initialize_file()

        self.task_list = self._load_tasks()

    def _initialize_file(self) -> None:
        """
        Initializes an empty file by creating a new JSON file with the name specified in `self.file_name`

        :rtype: None
        """
        initial_data = {"tasks": []}
        with open(self.file_name, 'w', encoding='UTF-8') as file:
            json.dump(initial_data, file, indent=4)

    def _load_tasks(self):
        try:
            with open(self.file_name, 'r', encoding='UTF-8') as file:
                data = json.load(file)
                return [
                    Task(
                        task.get('id'),
                        task.get('description'),
                        task.get('status'),
                        task.get('created_at'),
                        task.get('updated_at')
                    ) for task in data.get("tasks", [])
                ]
        except json.JSONDecodeError:
            print(f"Error reading {self.file_name}")
            exit(1)

    def _update_tasks(self):
        json_data = json.dumps({'tasks': [task.to_json() for task in self.task_list]})

        with open(self.file_name, 'w') as data:
            data.write(json_data)

    def _find_task(self, task_id: int):
        task = next((task for task in self.task_list if task.id == int(task_id)), None)

        if not task:
            raise KeyError(f"Task {task_id} not found.")

        return task

    def update_task(self, task_id: int, description: str):
        task = self._find_task(task_id)
        task.description = description
        self._update_tasks()

    def delete_task(self, task_id: int):
        task = self._find_task(task_id)
        self.task_list.remove(task)
        self._update_tasks()

    def add_task(self, description: str):
        if not description:
            raise ValueError("Description is required and should be a text")

        new_task_id = self.task_list[-1].id + 1 if len(self.task_list) > 0 else 1

        task = Task(task_id=new_task_id, description=description)
        self.task_list.append(task)
        self._update_tasks()

        print(f"Task added successfully (ID: {new_task_id})")

    def list_tasks(self):
        tasks = self._load_tasks()
        for task in tasks:
            print(task)
