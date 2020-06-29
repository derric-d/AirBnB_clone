#!/usr/bin/env python3
'''test module for the base model'''
import unittest
import uuid
from datetime import datetime
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

    def test_id(self):
        '''
        test id at init
        needs uuid module
        '''
        model_1 = BaseModel()
        model_2 = BaseModel()
        self.assertFalse(model_1.id == model_2.id)

    def test_create_update(self):
        '''
        test the create and update time
        needs datetime module
        '''
        start_time = datetime.utcnow()
        model_3 = BaseModel()
        end_time = datetime.utcnow()
        self.assertTrue(start_time <= model_3.created_at <= end_time)
        self.assertTrue(start_time <= model_3.updated_at <= end_time)

    def test_to_dict(self):
        '''
        test to_dict method for base
        '''
        model_4 = BaseModel()
        m4_dict = dict(model_4.__dict__)
        m4_dict['__class__'] = "BaseModel"
        m4_dict['created_at'] = m4_dict['created_at'].isoformat()
        m4_dict['updated_at'] = m4_dict['updated_at'].isoformat()
        self.assertEqual(m4_dict, model_4.to_dict)

    def test_str(self):
        '''
        test str rep of base
        '''
        model_5 = BaseModel()
        m5_str = "[BaseModel] ({}) {}".format(model_5.id, model_5.__dict__)
        self.assertEqual(m5_str, str(model_5))

if __name__ == "__main__":
    unittest.main()
