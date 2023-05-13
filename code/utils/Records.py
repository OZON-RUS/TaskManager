from datetime import date
from time import time


# Parent class for all types of Records
class Record:
    id_ = None

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

    def __init__(self, *args, **kwargs):
        super().__init__()
        for key, value in kwargs.items():
            self.__setattr__(key, value)
        self.id_ = self.name
