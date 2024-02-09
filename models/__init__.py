#!/usr/bin/python3
""" Initialize the packages."""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
