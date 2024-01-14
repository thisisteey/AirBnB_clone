#!/usr/bin/python3
"""A City class inherited from the BaseModel class is defined"""
from models.base_model import BaseModel


class City(BaseModel):
    """Representing the defined City class from the BaseModel class
    Attributes:
    state_id (str): the state id
    name (str): the name of the city"""
    state_id = ""
    name = ""
