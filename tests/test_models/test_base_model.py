#!/usr/bin/python3
""" Test for BaseModel class """
import unittest
from datetime import datetime, date, time
import uuid
from models import storage
from models.base_model import BaseModel
import os
import time

class TestBaseModel(unittest.TestCase):

    """tests for the BaseModel class"""

    def setUp(self):
        """to set it up"""
        pass

    def tearDown(self):
        """to tear it all down"""
        self.resetStorage()
        pass
