#!/usr/bin/python3
"""A Review class inherited from the BaseModel class is defined"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Representing the defined Review class from the BaseModel class
    Attributes:
    place_id (str): the id of the place
    user_id (str): the id of the user
    text (str): the review text or message"""
    place_id = ""
    user_id = ""
    text = ""
