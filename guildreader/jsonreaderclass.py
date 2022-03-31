"""
Data Storage and Retrieval from JSON objects with ID's
"""
from pathlib import Path
import logging

try:
    import ujson as json
except ImportError:  # Fall back
    logging.warning("`ujson` package is not installed large JSON objects will be accessed/modified slower")
    import json

class Reader:
    def __init__(self, directory: str, ids: list) -> None:
        if not (Path(directory).exists() and Path(directory).is_dir()):
            Path(directory).mkdir(parents=True) # Create the directories if needed
        self.directory = directory
        if not isinstance(ids, list):
            ids = list(ids) # Convert if its not a list
        self._ids = ids
        self.__defaults = {}

    def update_ids(self, ids: list):
        self._ids = ids # Update ID list

    def create_file(self, key: str, default = "", wipe: bool = False):
        """
        Creates a JSON config file for all ids it can see with a default
            Parameters:
                key (str): The `data_[key].json` to generate
                default (any): The value to put in as a placeholder
                wipe (bool): Wipe the files forcefully
            Returns:
                Success (bool): Did it succeed
        """
        if Path(f'{self.directory}/data_{key}.json').is_file() and not wipe: # allows for wiping of the config
            return False

        data = {}

        for id in self._ids:
            _id = str(id) # Make sure its a str for consistency
            data[_id] = default # Init with default value

        self.__defaults[key] = default # Store what the default was so we can repair if a id is missing

        with open(f'{self.directory}/data_{key}.json', 'w') as fileout:
            json.dump(data, fileout, indent=4)
        return True

    def read_file(self, id, key: str):
        """
        Reads a JSON file given the ID to find and key to look in
            Parameters:
                id (str/int): the ID to return given key
                key (str): The key to look up
            Returns:
                data(any): The data for that key/id pair
        """
        data = {}
        id= str(id)

        if not Path(f'{self.directory}/data_{key}.json').is_file():
            return False

        with open(f'{self.directory}/data_{key}.json', 'r') as filein:
            data = json.load(filein)

        try:
            return data[id]
        except KeyError:
            self._repair_id(id, key)

    def _repair_id(self, id, key):
        """
        Inits a ID in a key with the default value
        """
        id = str(id)
        if not Path(f'{self.directory}/data_{key}.json').is_file():
            return False

        with open(f'{self.directory}/data_{key}.json', 'r') as filein:
            data = json.load(filein)

        data[id] = self.__defaults[key]

        with open(f'{self.directory}/data_{key}.json', 'w') as fileout:
            json.dump(data, fileout, indent=4)
        return True

    def write_file(self, id, key: str, value):
        """
        Writes data to a key JSON given a id
            Parameters:
                id (str/int): ID to write to
                key (str): The key to modify
                value (any): The value to write for that key/id pair
            Returns:
                Success (bool): Did it succeed
        """
        data = {}
        id = str(id)

        if not Path(f'{self.directory}/data_{key}.json').is_file():
            return False

        with open(f'{self.directory}/data_{key}.json', 'r') as filein:
            data = json.load(filein)

        data[id] = value

        with open(f'{self.directory}/data_{key}.json', 'w') as fileout:
            json.dump(data, fileout, indent=4)
        return True

    def remove(self, id, key: str):
        """
        Removes a id from a given key
            Parameters:
                id (str/int): ID to remove
                key (str): The key to modify
            Returns:
                Success (bool): Did it succeed
        """
        data = {}
        id = str(id)

        if not Path(f'{self.directory}/data_{key}.json').is_file():
            return False

        with open(f'{self.directory}/data_{key}.json', 'r') as filein:
            data = json.load(filein)

        data.pop(id)

        with open(f'{self.directory}/data_{key}.json', 'w') as fileout:
            json.dump(data, fileout, indent=4)

        return True

    def check_exist(self, key: str):
        """
        Checks if a JSON key has been generated yet
            Parameters:
                key (str): The key to check
            Returns:
                Exist (bool): Does it exist
        """
        return Path(f'{self.directory}/data_{key}.json').is_file()


    def dump(self, key: str):
        """
        Dumps all the JSON given the key
            Parameters:
                key (str): The key to dump
            Returns:
                data (dict): The JSON data
        """
        data = {}

        with open(f'{self.directory}/data_{key}.json', 'r') as filein:
            data = json.load(filein)

        return data

Reader(".\\test")