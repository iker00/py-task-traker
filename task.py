import json
from datetime import datetime


class Task:
    def __init__(self, task_id: str, description: str, status: bool = False, created_at: datetime = None,
                 updated_at: datetime = None):
        self.id = task_id
        self.description = description
        self.status = status
        self.created_at = created_at if created_at else datetime.now()
        self.updated_at = updated_at if updated_at else datetime.now()

    def is_done(self):
        return self.status

    def update_status(self, new_status: bool):
        self.status = new_status
        self.updated_at = datetime.now()

    def to_json(self):
        data = {key: (value.isoformat() if isinstance(value, datetime) else value)
                for key, value in self.__dict__.items()}
        return data
