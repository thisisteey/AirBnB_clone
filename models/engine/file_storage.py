#!/usr/bin/python3
"""A FileStorage class of the HBnB project is defined"""
import json
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Representing the define FileStorage of the HBnB project
    Private Class Attributes:
    __file_path (str): designated file name to save objects
    __objects (dict): dictionary containing instaces of objects"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """gets and returns the dictionary of __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """assigns obj in __objects with key <obj_class_name>.id"""
        objclsname = obj.__class__.__name__
        key = f"{objclsname}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serialize the contents of __objects to the JSON file"""
        objdict = FileStorage.__objects
        serobj = {obj: objdict[obj].to_dict() for obj in objdict.keys()}
        with open(FileStorage.__file_path, "w") as fl:
            json.dump(serobj, fl)

    def reload(self):
        """deserialize the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path) as fl:
                serobj = json.load(fl)
                for serobjdt in serobj.values():
                    clsname = serobjdt["__class__"]
                    del serobjdt["__class__"]
                    self.new(eval(clsname)(**serobjdt))
        except FileNotFoundError:
            return
