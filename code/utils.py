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

    def edit(self, *args, **kwargs):
        pass

    def delete(self):
        pass


class Task(Record):
    '''
    To be implemented:
    subTasks: []
    is_frequent: bool
    '''
    priority: int
    deadline: date
    description: str
    start_date: date
    start_time: time
    time_to_complete: time

    def __init__(self, *args, **kwargs):
        super(Task, self).__init__(*args, **kwargs)
        for key, value in kwargs.items():
            self.__setattr__(key, value)

