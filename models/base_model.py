#!/usr/bin/python3
"""A BaseModel class of the HBnB project is defined"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Representing the defined BaseModel of the HBnB project"""

    def __init__(self, *args, **kwargs):
        """Initializing the BaseModel class
        Args:
        *args: Unused
        **kwargs (dict): key/value pairs of attributes"""
        dtfmt = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if kwargs:
            for key, val in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    self.__dict__[key] = datetime.strptime(val, dtfmt)
                else:
                    self.__dict__[key] = val
        else:
            models.storage.new(self)

    def __str__(self):
        """gets and returns the string representation of the BaseModel"""
        clsname = self.__class__.__name__
        return f"[{clsname}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates 'updated_at' with the recent datetime and save to storage"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """generates the dictionary representation of the BaseModel instance"""
        dictrep = self.__dict__.copy()
        dictrep["created_at"] = self.created_at.isoformat()
        dictrep["updated_at"] = self.updated_at.isoformat()
        dictrep["__class__"] = type(self).__name__
        return dictrep
