#!/usr/bin/python3
"""Unittest for file_storage.py is defined"""
import unittest
import models
from datetime import datetime
from os import rename, remove


class TestFileStorageinstance(unittest.TestCase):
    """Unittests for creating instances of the FileStorage class"""

    def testFileStorageinstancenoargs(self):
        """test FileStorage instance with no arguments"""
        self.assertEqual(type(models.FileStorage()), models.FileStorage)

    def testFileStorageinstanceargs(self):
        """test FileStorage instance with arguments"""
        self.assertRaises(TypeError, lambda: models.FileStorage(None))

    def testFileStorage__file_pathattr(self):
        """test FileStorage __file_path attr is a private string"""
        self.assertEqual(str, type(models.FileStorage._FileStorage__file_path))

    def testFileStorage__objectsattr(self):
        """test FileStorage __objects attr is a private dict"""
        self.assertEqual(dict, type(models.FileStorage._FileStorage__objects))

    def testFileStorage_storageinitialize(self):
        """test FileStorage storage attr initialize as Filestorage inst"""
        self.assertEqual(type(models.storage), models.FileStorage)


class TestFileStoragemethods(unittest.TestCase):
    """Unittest for FileStorage methods"""

    @classmethod
    def setUp(self):
        """setUp environment for the 'methods' tests"""
        try:
            rename("file.json", "tmpfile")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        """clean up environment after the 'methods' tests"""
        try:
            remove("file.json")
        except IOError:
            pass
        try:
            rename("tmpfile", "file.json")
        except IOError:
            pass
        models.FileStorage._FileStorage__objects = {}

    def testallmethods(self):
        """test 'all methods' returns a dictionary"""
        self.assertEqual(dict, type(models.storage.all()))

    def testallmethodsargs(self):
        """test 'all methods' with an argument or arguments"""
        self.assertRaises(TypeError, lambda: models.storage.all(None))

    def testnewmethods(self):
        """test that 'new method' creates instances and adds to storage"""
        instances = {
            "BaseModel": models.base_model.BaseModel(),
            "User": models.user.User(),
            "State": models.state.State(),
            "City": models.city.City(),
            "Amenity": models.amenity.Amenity(),
            "Place": models.place.Place(),
            "Review": models.review.Review()
        }
        for clsname, instance in instances.items():
            models.storage.new(instance)
            key = f"{clsname}.{instance.id}"
            self.assertIn(key, models.storage.all().keys())
            self.assertIn(instance, models.storage.all().values())

    def testnewmethodsargs(self):
        """test the 'new method' with arguments"""
        instance = {"BaseModel": models.base_model.BaseModel()}
        self.assertRaises(TypeError, lambda: models.storage.new(instance, 1))

    def testsavemethods(self):
        """test that 'save method' saves storage of instances to a file"""
        instances = {
            "BaseModel": models.base_model.BaseModel(),
            "User": models.user.User(),
            "State": models.state.State(),
            "City": models.city.City(),
            "Amenity": models.amenity.Amenity(),
            "Place": models.place.Place(),
            "Review": models.review.Review()
        }
        for clsname, instance in instances.items():
            models.storage.new(instance)
        models.storage.save()
        with open("file.json", "r") as fl:
            svtext = fl.read()
            for clsname, instance in instances.items():
                key = f"{clsname}.{instance.id}"
                self.assertIn(key, svtext)

    def testsavemethodsargs(self):
        """test the 'save method' with arguments"""
        self.assertRaises(TypeError, lambda: models.storage.save(None))

    def testreloadmethods(self):
        """test that 'reload methods' reloads storage and has objs"""
        instances = {
            "BaseModel": models.base_model.BaseModel(),
            "User": models.user.User(),
            "State": models.state.State(),
            "City": models.city.City(),
            "Amenity": models.amenity.Amenity(),
            "Place": models.place.Place(),
            "Review": models.review.Review()
        }
        for clsname, instance in instances.items():
            models.storage.new(instance)
        models.storage.save()
        models.storage.reload()
        objs = models.FileStorage._FileStorage__objects
        for clsname, instance in instances.items():
            key = f"{clsname}.{instance.id}"
            self.assertIn(key, objs)

    def testreloadmethodsargs(self):
        """test the 'reload methods' with arguments"""
        self.assertRaises(TypeError, lambda: models.storage.reload(None))


if __name__ == "__main__":
    unittest.main()
