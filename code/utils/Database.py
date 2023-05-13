import json
from utils.Records import Record


# Parent class for all the classes of file saving
class SaveToFile:

    # File for saving
    _file = None

    # Object constructor
    def __init__(self, filename: str):
        try:
            # If file do exist open in r+ mode
            self._file = open(filename, 'r+')
        except OSError:
            # If file doesn't exist open in w+ mode and create it
            self._file = open(filename, 'w+')

        # File wasn't created
        if self._file is None:
            # Make error handling
            print(f"{filename} file can't be opened")
            del self

    # Object destructor
    def __del__(self):
        self._file.close()
        del self._file

    def save(self, value: str):
        pass

    # Clear all the file content
    def clear_file(self):
        filename = self._file.name
        self._file.close()
        self._file = open(filename, 'w+')

        if self._file is None:
            # Make error handling
            print(f"{filename} file can't be opened. OSError exception")
            del self


# Parent class for all the classes of database saving
class SaveToDatabase(SaveToFile):
    def __init__(self, filename: str):
        super(SaveToDatabase, self).__init__(filename)


# Saves the object into SQL database
class SaveToSQL(SaveToDatabase):
    pass


# Saves the object into no SQL database
class SaveToNoSQL(SaveToDatabase):
    def __init__(self, filename: str):
        super(SaveToNoSQL, self).__init__(filename)


class SaveToJSON(SaveToNoSQL):

    def __init__(self, filename: str):
        super(SaveToNoSQL, self).__init__(filename)

    def save(self, record: Record):
        record_properties: dict

        # Load dict from file
        try:
            record_properties = json.load(self._file)
        # Parse Error
        except json.JSONDecodeError:
            # init dict with null dict of properties of Record with {_id}
            record_properties = {record.__getattribute__("_id"): {}}
            print("Error Parse")
        # Create null dict of properties of Record with {_id}
        finally:
            record_properties[record.__getattribute__("_id")] = {}

        # Add properties in the dict
        for var in dir(record):
            if var.strip('_') == var:
                record_properties[record.__getattribute__("_id")][var] = record.__getattribute__(var)

        # Clear file before write in it
        self.clear_file()
        print(self._file)
        # Save dict in file
        json.dump(record_properties, self._file)
