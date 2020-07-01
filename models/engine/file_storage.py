#!/usr/bin/python3
"""
Define a FileStorage class.
"""
import json
import os.path
from datetime import datetime, date, time
from models.base_model import BaseModel
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.user import User
from models.state import State
from models.review import Review


class FileStorage:
    """Define class FileStorage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Set object with obj class name.id"""
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """Serialize objects to JSON file"""
        with open(self.__file_path, 'w') as f:
            new_dict = {key: obj.to_dict() for key, obj in
                        self.__objects.items()}
            json.dump(new_dict, f)

    def reload(self):
        """Deserialize JSON file to objects"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as f:
                for key, value in json.load(f).items():
                    self.__objects[key] = eval(key.split('.')[0])(**value)
