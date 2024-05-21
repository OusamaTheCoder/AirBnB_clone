#!/usr/bin/python3
"""
This script initializes the FileStorage instance and loads existing data.
"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
