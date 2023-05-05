from .. import utils

def create_task(*args, **kwargs):
    Task = utils.Task(*args, **kwargs)
    return Task