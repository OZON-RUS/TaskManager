from utils import Database
from utils import Records


def create_task(*args, **kwargs):
    task = Records.Task(*args, **kwargs)

    file = Database.SaveToJSON("task.json")
    if file is None:
        print("Database upload attempt failed")
        return None

    file.save(task)
    # Realize error handling
    return task
