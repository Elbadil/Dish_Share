#!/usr/bin/python3
"""DBstorage Engine Instance"""
from models.engine.db_storage import DBstorage


storage = DBstorage()
storage.reload()
