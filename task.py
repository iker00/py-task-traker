from status import Status
from datetime import datetime


class Task:
    def __init__(self, task_id: int, description: str, status: Status = Status.NOT_DONE, created_at: str = None,
                 updated_at: str = None):
        self.id = task_id
        self.description = description
        self.status = status
        self.created_at = datetime.fromisoformat(created_at) if created_at else datetime.now()
        self.updated_at = datetime.fromisoformat(updated_at) if updated_at else datetime.now()

    def is_done(self):
        return self.status

    def update_status(self, new_status: Status):
        self.status = new_status
        self.updated_at = datetime.now()

    def to_json(self):
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status if type(self.status) is not Status else self.status.value,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

    def __str__(self):
        return f"{self.description} (ID: {self.id})"
