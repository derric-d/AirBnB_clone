#!/usr/bin/env python3
'''test module for the Amenity model'''
import unittest
import uuid
from datetime import datetime
from models.place import Place
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    '''
    test for user model class
    '''
    def test_new_place(self):
        '''
        test base case
        '''
        new_p = Place()
        self.assertTrue(issubclass(Place, BaseModel))
        new_p.name = "betty"
        new_p.my_number = 12
        self.assertEqual([new_p.name, new_p.my_number], ["betty", 12])

    def test_user_init(self):
        '''
        test for init
        '''
        new_a = Place()
        self.assertTrue(hasattr(new_a, "id"))
        self.assertTrue(hasattr(new_a, "created_at"))
        self.assertTrue(hasattr(new_a, "updated_at"))
        self.assertTrue(hasattr(new_a, "name"))

        self.assertTrue(hasattr(new_a, "city_id"))
        self.assertTrue(hasattr(new_a, "user_id"))
        self.assertTrue(hasattr(new_a, "description"))
        self.assertTrue(hasattr(new_a, "number_rooms"))
        self.assertTrue(hasattr(new_a, "number_bathrooms"))
        self.assertTrue(hasattr(new_a, "max_guest"))
        self.assertTrue(hasattr(new_a, "price_by_night"))

        self.assertTrue(hasattr(new_a, "latitude"))
        self.assertTrue(hasattr(new_a, "longitude"))
        self.assertTrue(hasattr(new_a, "amenity_ids"))

    def test_user_id(self):
        '''
        test that id is created correctly
        '''
        a_3 = Place()
        a_4 = Place()
        self.assertFalse(a_3.id == a_4.id)

    def test_user_time(self):
        '''
        test for create/update time
        '''
        start = datetime.utcnow()
        a_2 = Place()
        end = datetime.utcnow()
        self.assertTrue(start <= a_2.created_at <= end)
        self.assertTrue(start <= a_2.updated_at <= end)

    def test_to_dict(self):
        '''
        test to_dict method for base
        '''
        a_5 = Place()
        a5_dict = dict(a_5.__dict__)
        a5_dict['__class__'] = "Place"
        a5_dict['created_at'] = a5_dict['created_at'].isoformat()
        a5_dict['updated_at'] = a5_dict['updated_at'].isoformat()
        self.assertEqual(a5_dict, a_5.to_dict())

    def test_str(self):
        '''
        test str rep of base
        '''
        a_6 = Place()
        a6_str = "[Place] ({}) {}".format(a_6.id, a_6.__dict__)
        self.assertEqual(a6_str, str(a_6))

    def test_attr(self):
        '''
        test amenity attributes --just name as str
        '''
        self.assertEqual(type(Place.name), str)
        self.assertEqual(type(Place.city_id), str)

        self.assertEqual(type(Place.user_id), str)
        self.assertEqual(type(Place.description), str)
        self.assertEqual(type(Place.number_rooms), int)
        self.assertEqual(type(Place.number_bathrooms), int)
        self.assertEqual(type(Place.max_guest), int)
        self.assertEqual(type(Place.price_by_night), int)

        self.assertEqual(type(Place.latitude), float)
        self.assertEqual(type(Place.longitude), float)
        self.assertEqual(type(Place.amenity_ids), list)
