from console_creator import *
import controller
from utils import utils

def create_task():
    kwargs = {}
    for var in dir(utils.Task):
        if var.strip('_') == var:
            kwargs[var] = input(f"\t{var}: ")
    task = controller.create_task(**kwargs)
    print(task)

console = Console(exit_aliases=("exit",), lowercase_commands=True, end_message=None)

CREATE_TASK_DESCRIPTION = "This command creates a Task record"
console.add_command(Command("create_task", create_task, description=CREATE_TASK_DESCRIPTION))

console.launch()
