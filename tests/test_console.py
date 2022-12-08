#!/usr/bin/python3
"""A unittest module for the cmd"""
import os
import MySQLdb
import sqlalchemy
import unittest
import json
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from test import clear_stream
