import sys
from task import Task
from task_manager import TaskManager


def main():
    if len(sys.argv) < 2:
        print("Por favor, proporciona un argumento")
        sys.exit(1)

    arg = sys.argv[1]
    tm = TaskManager()

    try:
        match arg:
            case "add":
                description = sys.argv[2] if len(sys.argv) > 2 else False
                task_id = tm.add_task(description=description)
                print(f"Task added successfully (ID: {task_id})")
            case "update":
                pass
            case "list":
                pass
            case "delete":
                pass
            case _:
                print("Invalid arg")
    except ValueError as exception:
        print(exception)


def add_task(description: str):
    task = Task(task_id="1", description=description)
    return task.id


if __name__ == "__main__":
    main()
