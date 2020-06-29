#!/usr/bin/env python3
'''test module for the user model'''
import unittest
import uuid
from datetime import datetime
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    '''
    test for user model class
    '''
    def test_new_user(self):
        '''
        test base case
        '''
        new_user = User()
        self.assertTrue(issubclass(User, BaseModel))
        new_user.name = "betty"
        new_user.my_number = 12
        self.assertEqual([new_user.name, new_user.my_number], ["betty", 12])

    def test_user_init(self):
        '''
        test for init
        '''
        user_1 = User()
        self.assertTrue(hasattr(user_1, "id"))
        self.assertTrue(hasattr(user_1, "created_at"))
        self.assertTrue(hasattr(user_1, "updated_at"))
        self.assertTrue(hasattr(user_1, "email"))
        self.assertTrue(hasattr(user_1, "password"))
        self.assertTrue(hasattr(user_1, "first_name"))
        self.assertTrue(hasattr(user_1, "last_name"))

    def test_user_id(self):
        '''
        test that id is created correctly
        '''
        user_3 = User()
        user_4 = User()
        self.assertFalse(user_3.id == user_4.id)

    def test_user_time(self):
        '''
        test for create/update time
        '''
        start = datetime.utcnow()
        user_2 = User()
        end = datetime.utcnow()
        self.assertTrue(start <= user_2.created_at <= end)
        self.assertTrue(start <= user_2.updated_at <= end)

    def test_to_dict(self):
        '''
        test to_dict method for base
        '''
        user_5 = User()
        u5_dict = dict(user_5.__dict__)
        u5_dict['__class__'] = "User"
        u5_dict['created_at'] = u5_dict['created_at'].isoformat()
        u5_dict['updated_at'] = u5_dict['updated_at'].isoformat()
        self.assertEqual(u5_dict, user_5.to_dict)

    def test_str(self):
        '''
        test str rep of base
        '''
        user_6 = User()
        u6_str = "[User] ({}) {}".format(user_6.id, user_6.__dict__)
        self.assertEqual(u6_str, str(user_6))

    def test_attr(self):
        '''
        test attributes types of user class
        --all strings--
        '''
        self.assertEqual(type(User.email), str)
        self.assertEqual(type(User.password), str)
        self.assertEqual(type(User.first_name), str)
        self.assertEqual(type(User.last_name), str)

if __name__ = "__main__":
    unittest.main()
