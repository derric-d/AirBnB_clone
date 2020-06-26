#!/usr/bin/env python3
'''test module for the base model'''
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    '''unit test for base model'''

    def test_init(self):
        '''
        test creation of instance attr on init
        '''
        new_base = BaseModel()
        self.assertTrue(hasattr(new_base, "id"))
        self.assertTrue(hasattr(new_base, "created_at"))
        self.assertTrue(hasattr(new_base, "updated_at"))

    """
    test_id
    test_created_at && _updated_at
    test_to_dict
    test_str_
    """
