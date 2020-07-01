#!/usr/bin/python3
"""AirBnB Base Model"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """define BaseModel class"""

    def __init__(self, *args, **kwargs):
        """initialize BaseModel instance"""
        if (kwargs):
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """str representation of BaseModel"""

        return ('[' + str(type(self).__name__) + '] (' + str(self.id) +
                ') ' + str(self.__dict__))

    def save(self):
        """Update updated_at attribute"""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return dictionary containing keys/values of __dict__"""
        base_dict = self.__dict__.copy()
        base_dict.update({'__class__': str(type(self).__name__)})
        base_dict["__class__"] = self.__class__.__name__
        base_dict['created_at'] = self.created_at.isoformat()
        base_dict['updated_at'] = self.updated_at.isoformat()
        return base_dict
