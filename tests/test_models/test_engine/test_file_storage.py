#!/usr/bin/env python
'''test for filestorage module'''
import unittest
import json
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):
    '''
    class for test of file storage module
    tests for
    all method -- returns dict and format of dict
    new method -- adds new pair to object/file storage instance
    save -- test stoarage and extraction of storage file
    '''
    temp_path = ""
    fs_attr = FileStorage()

    def setUp(self):
        '''init filestorage instance for test case'''
        FileStorage._FileStorage__objects = {}
        TestFileStorage.temp_path = FileStorage._FileStorage__file_path
        FileStorage._FileStorage__file_path = "file.json"

    def tearDown(self):
        '''delete file for filestorage'''
        try:
            os.remove('file.json')
        except:
            pass
        FileStorage._FileStorage__file_path = TestFileStorage.temp_path

    def testAll(self):
        '''
        test all() should return dict
        '''
        test_store = FileStorage()
        new_base = BaseModel()
        test_store.new(new_base)
        self.assertEqual(type(test_store.all()), dict)

    def testDictObj(self):
        '''
        test all() returns valid dict contents
        '''
        new_dict = {"BaseModel.1234": {"att1": 1, "att2": 2},
                    "BaseModel.4321": {"att3": 3, "att4": 4}}
        FileStorage._FileStorage__objects = new_dict
        self.assertEqual(new_dict,
                         TestFileStorage.fs_attr.all())

    def testNew(self):
        '''
        test new() adds pair to storage instance
        '''
        test_s = FileStorage()
        new_base = BaseModel()
        test_s.new(new_base)
        self.assertEqual(type(test_s.all()), dict)
        self.assertEqual(len(test_s.all()), 1)
        self.assertEqual(test_s.all()
                         ["BaseModel.{}".format(new_base.id)], new_base)

    def testSave(self):
        '''
        test save() storage
        '''
        new_base1 = BaseModel()
        new_base2 = BaseModel()
        FileStorage().new(new_base1)
        FileStorage().new(new_base2)
        FileStorage().save()
        self.assertTrue(os.path.exists('file.json'))
        with open("file.json", "r") as file:
            self.assertEqual(json.loads(file.read()),
                             {key: val.to_dict()
                                 for key, val in
                                 FileStorage().all().items()})

    def testRelaod(self):
        '''
        test reload() data can be saved to and loadedfrom json
        '''
        f = storage._FileStorage__file_path
        self.assertFalse(os.path.exists(f))
        storage.reload()
        self.assertFalse(storage.all())
        new_base1 = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists(f))
        with open(f, "r") as file:
            loaded_json = json.load(file)
        cmp_json = {key: val.to_dict()
                    for key, val in storage.all().items()}
        self.assertEqual(cmp_json, loaded_json)
