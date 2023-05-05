from datetime import date
from time import time


class SaveToFile:
    _filename: str
    _obj: object


class SaveToDatabase(SaveToFile):
    pass


class SaveToSQL(SaveToDatabase):
    pass


class SaveToNonSQL(SaveToDatabase):
    pass


class Record:

    def _edit(self, *args, **kwargs):
        pass

    def _delete(self):
        pass


class Task(Record):
    '''
    To be implemented:
    subTasks: []
    is_frequent: bool
    '''
    priority: int = None
    deadline: date = None
    description: str = None
    start_date: date = None
    start_time: time = None
    time_to_complete: time = None

    def __init__(self, *args, **kwargs):
        #FIX
        #super(Task, self).__init__(*args, **kwargs)
        for key, value in kwargs.items():
            self.__setattr__(key, value)
        return
