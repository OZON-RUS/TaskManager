from datetime import date
from time import time


# Parent class for all types of Records
class Record:
    _id = None

    def _edit(self, *args, **kwargs):
        pass

    def _delete(self):
        pass


# Task to be done
class Task(Record):
    name: str = None
    description: str = None
    date: date = None
    time: time = None
    isComplete: bool

    # Object constructor
    def __init__(self, *args, **kwargs):
        super().__init__()
        # init all the Task properties
        for key, value in kwargs.items():
            self.__setattr__(key, value)
        self._id = self.name
