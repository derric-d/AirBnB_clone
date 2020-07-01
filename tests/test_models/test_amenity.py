#!/usr/bin/env python3
'''test module for the Amenity model'''
import unittest
import uuid
from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    '''
    test for user model class
    '''
    def test_new_user(self):
        '''
        test base case
        '''
        new_a = Amenity()
        self.assertTrue(issubclass(Amenity, BaseModel))
        new_a.name = "betty"
        new_a.my_number = 12
        self.assertEqual([new_a.name, new_a.my_number], ["betty", 12])

    def test_user_init(self):
        '''
        test for init
        '''
        new_a = Amenity()
        self.assertTrue(hasattr(new_a, "id"))
        self.assertTrue(hasattr(new_a, "created_at"))
        self.assertTrue(hasattr(new_a, "updated_at"))
        self.assertTrue(hasattr(new_a, "name"))

    def test_user_id(self):
        '''
        test that id is created correctly
        '''
        a_3 = Amenity()
        a_4 = Amenity()
        self.assertFalse(a_3.id == a_4.id)

    def test_user_time(self):
        '''
        test for create/update time
        '''
        start = datetime.utcnow()
        a_2 = Amenity()
        end = datetime.utcnow()
        self.assertTrue(start <= a_2.created_at <= end)
        self.assertTrue(start <= a_2.updated_at <= end)

    def test_to_dict(self):
        '''
        test to_dict method for base
        '''
        a_5 = Amenity()
        a5_dict = dict(a_5.__dict__)
        a5_dict['__class__'] = "Amenity"
        a5_dict['created_at'] = a5_dict['created_at'].isoformat()
        a5_dict['updated_at'] = a5_dict['updated_at'].isoformat()
        self.assertEqual(a5_dict, a_5.to_dict())

    def test_str(self):
        '''
        test str rep of base
        '''
        a_6 = Amenity()
        a6_str = "[Amenity] ({}) {}".format(a_6.id, a_6.__dict__)
        self.assertEqual(a6_str, str(a_6))

    def test_attr(self):
        '''
        test amenity attributes --just name as str
        '''
        self.assertEqual(type(Amenity.name), str)

if __name__ == "__main__":
    unittest.main()
