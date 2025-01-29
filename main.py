import sys
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
                tm.add_task(description=get_arg(2))
            case "update":
                tm.update_task(task_id=get_arg(2), description=get_arg(3))
            case "list":
                tm.list_tasks()
            case "delete":
                tm.delete_task(task_id=get_arg(2))
            case _:
                print("Invalid arg")
    except (ValueError, KeyError) as exception:
        print(exception)

def get_arg(arg_index: int):
    return sys.argv[arg_index] if len(sys.argv) > arg_index else False


if __name__ == "__main__":
    main()
