from utils import utils

def create_task(*args, **kwargs):
    task = utils.Task(*args, **kwargs)
    return task