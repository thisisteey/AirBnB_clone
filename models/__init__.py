#!/usr/bin/python3
"""Intialize module-wide global variables (Singleton) Pattern"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
