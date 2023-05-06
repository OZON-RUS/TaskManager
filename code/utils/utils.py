from datetime import date
from time import time

# Parent class for all the classes of file saving
class SaveToFile:
    _filename: str
    _obj: object


# Parent class for all the classes of database saving
class SaveToDatabase(SaveToFile):
    pass


# Saves the object into SQL database
class SaveToSQL(SaveToDatabase):
    pass


# Saves the object into non SQL database
class SaveToNonSQL(SaveToDatabase):
    pass


# Parent class for all types of Records
class Record:

    def _edit(self, *args, **kwargs):
        pass

    def _delete(self):
        pass

# Task to be done
class Task(Record):
    """
    To be implemented:
    subTasks: []
    is_frequent: bool
    """
    priority: int = None
    deadline: date = None
    description: str = None
    start_date: date = None
    start_time: time = None
    time_to_complete: time = None

    def __init__(self, *args, **kwargs):
        super().__init__()
        for key, value in kwargs.items():
            self.__setattr__(key, value)
        return
