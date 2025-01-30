import sys
from task_manager import TaskManager


def main():
    if len(sys.argv) < 2:
        print("Please insert a command argument: 'add', 'list', 'update' or 'delete'")
        sys.exit(1)

    arg = sys.argv[1]
    task_manager = TaskManager()

    try:
        match arg:
            case "add":
                task_manager.add_task(description=get_arg(2))
            case "update":
                task_manager.update_task(task_id=get_arg(2), description=get_arg(3))
            case "list":
                task_manager.list_tasks()
            case "delete":
                task_manager.delete_task(task_id=get_arg(2))
            case _:
                print("Invalid arg")
    except (ValueError, KeyError) as exception:
        print(exception)

def get_arg(arg_index: int) -> str|False:
    """
    Get command-line argument at the specified position.

    :param arg_index: The index of the argument.
    :return: The argument value if exists, or False if not exists.
    """
    return sys.argv[arg_index] if len(sys.argv) > arg_index else False


if __name__ == "__main__":
    main()
