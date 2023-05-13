from console_creator import *
import controller
from utils import Records


# Function to create a task
def create_task():

    # Non-positional arguments fot Task object initialization
    kwargs = {}

    # Loop for getting properties list of Task's class, setting them up and saving it in kwargs
    for var in dir(Records.Task):
        if var.strip('_') == var:
            kwargs[var] = input(f"\t{var}: ")

    # Use controller to connect with core
    task = controller.create_task(**kwargs)
    print(task)


if __name__ == "__main__":
    # Console_creator docs:
    # https://github.com/megat69/Lib_ConsoleCreator
    console = Console(exit_aliases=("exit",), lowercase_commands=True, end_message=None)

    CREATE_TASK_DESCRIPTION = "This command creates a Task record"
    console.add_command(Command("create_task", create_task, description=CREATE_TASK_DESCRIPTION))

    console.launch()




