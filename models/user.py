#!/usr/bin/python3
"""A User class inherited from the BaseModel class is defined"""
from models.base_model import BaseModel


class User(BaseModel):
    """Representing the defined User class from the BaseModel class
    Attributes:
    email (str): the email of the user
    password (str): the password of the user
    first_name (str): the first name of the user
    last_name (str): the last name of the user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
