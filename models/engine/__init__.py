#!/usr/bin/python3
"""This module instantiates an object of class FileStorage or DBStorage"""
from os import environ

from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

HBNB_TYPE_STORAGE = environ.get('HBNB_TYPE_STORAGE')

if HBNB_TYPE_STORAGE == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
