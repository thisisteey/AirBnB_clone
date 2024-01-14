#!/usr/bin/python3
"""Unittest for amenity.py is defined"""
import unittest
import time
import models
from os import rename, remove
from datetime import datetime
from models.amenity import Amenity


class TestAmenityinstance(unittest.TestCase):
    """Unittest for creating instances of the Amenity class"""

    def testAmenityinstancenoargs(self):
        """test Amenity instance with no arguments"""
        self.assertEqual(type(Amenity()), Amenity)

    def testAmenitynewinstancestorage(self):
        """test Amenity instances are stored in objects set"""
        self.assertIn(Amenity(), models.storage.all().values())

    def testAmenityidattr(self):
        """test if Amenity 'id' attr is a public string"""
        self.assertEqual(str, type(Amenity().id))

    def testAmenitycreated_atattr(self):
        """test if Amenity 'created_at' attr is a pub datetime obj"""
        self.assertEqual(datetime, type(Amenity().created_at))

    def testAmenityupdated_atattr(self):
        """test if Amenity 'updated_at' attr is a pub datetime obj"""
        self.assertEqual(datetime, type(Amenity().updated_at))

    def testAmenitynameattr(self):
        """test if Amenity 'name' is a public class attribute"""
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", Amenity().__dict__)

    def testAmenitytwoids(self):
        """test that two Amenity instances have unique 'ids'"""
        amty1 = Amenity()
        amty2 = Amenity()
        self.assertNotEqual(amty1.id, amty2.id)

    def testAmenitytwocreated_at(self):
        """test the 'created_at' timestamp of two Amenity instances"""
        amty1 = Amenity()
        time.sleep(0.07)
        amty2 = Amenity()
        self.assertLess(amty1.created_at, amty2.created_at)

    def testAmenitytwoupdated_at(self):
        """test the 'updated_at' timestamp of two Amenity instances"""
        amty1 = Amenity()
        time.sleep(0.07)
        amty2 = Amenity()
        self.assertLess(amty1.updated_at, amty2.updated_at)

    def testAmenitystrrep(self):
        """test the string representation of a Amenity instance"""
        currdt = datetime.today()
        dtrepr = repr(currdt)
        amty = Amenity()
        amty.id = "13579"
        amty.created_at = amty.updated_at = currdt
        amtystr = amty.__str__()
        self.assertIn("[Amenity] (13579)", amtystr)
        self.assertIn("'id': '13579'", amtystr)
        self.assertIn("'created_at': " + dtrepr, amtystr)
        self.assertIn("'updated_at': " + dtrepr, amtystr)

    def testAmenityunusedargs(self):
        """test that unused arguments do not affect HaseModel instances"""
        self.assertNotIn(None, Amenity(None).__dict__.values())

    def testAmenityinstancekwargs(self):
        """test Amenity instantiation with specified keywordargs(kwargs)"""
        currdt = datetime.today()
        dtiso = currdt.isoformat()
        amty = Amenity(id="246", created_at=dtiso, updated_at=dtiso)
        self.assertEqual(amty.id, "246")
        self.assertEqual(amty.created_at, currdt)
        self.assertEqual(amty.updated_at, currdt)

    def testAmenityinstanceNonekwargs(self):
        """test Amenity instantiation with None as kwargs"""
        self.assertRaises(TypeError, lambda: Amenity(id=None,
                          created_at=None, updated_at=None))


class TestAmenitysave(unittest.TestCase):
    """Unittest for the save method of the Amenity class"""

    @classmethod
    def setUp(self):
        """setUp environment for the 'save' method tests"""
        try:
            rename("file.json", "tmpfile")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        """clean up environment after the 'save' method tests"""
        try:
            remove("file.json")
        except IOError:
            pass
        try:
            rename("tmpfile", "file.json")
        except IOError:
            pass

    def testAmenityonesave(self):
        """test that Amenity 'save' call updates 'updated_at' timestamp"""
        amty = Amenity()
        time.sleep(0.08)
        fstupdated_at = amty.updated_at
        amty.save()
        self.assertLess(fstupdated_at, amty.updated_at)

    def testAmenitytwosaves(self):
        """test two Amenity 'save' calls updates 'updated_at' timestamps"""
        amty = Amenity()
        time.sleep(0.08)
        fstupdated_at = amty.updated_at
        amty.save()
        scdupdated_at = amty.updated_at
        self.assertLess(fstupdated_at, scdupdated_at)
        time.sleep(0.08)
        amty.save()
        self.assertLess(scdupdated_at, amty.updated_at)

    def testAmenitysaveargs(self):
        """test Amenity 'save' call with arguments"""
        self.assertRaises(TypeError, lambda: Amenity().save(None))

    def testAmenitysaveJSONfile(self):
        """test Amenity 'save' call updates the corresponding JSON file"""
        amty = Amenity()
        amty.save()
        amtyid = "Amenity." + amty.id
        with open("file.json", "r") as fl:
            self.assertIn(amtyid, fl.read())


class TestAmenityto_dict(unittest.TestCase):
    """Unittest for the 'to_dict' method of the Amenity class"""

    def testAmenityto_dcittype(self):
        """test Amenity 'to_dict' output is a dictionary"""
        self.assertTrue(dict, type(Amenity().to_dict()))

    def testAmenityto_dictkeys(self):
        """test Amenity 'to_dict' dictionary contains the correct keys"""
        self.assertIn("id", Amenity().to_dict())
        self.assertIn("created_at", Amenity().to_dict())
        self.assertIn("updated_at", Amenity().to_dict())
        self.assertIn("__class__", Amenity().to_dict())

    def testBasemodelto_dictaddattr(self):
        """test that Amenity 'to_dict' dict has additional attributes"""
        amty = Amenity()
        amty.name = "Taiwo_and_Olamide"
        amty.number = 147
        self.assertIn("name", amty.to_dict())
        self.assertIn("number", amty.to_dict())

    def testAmenityto_dictdatetimeattr(self):
        """test Amenity 'to_dict' dict datetime attr are string reps"""
        amtydict = Amenity().to_dict()
        self.assertEqual(str, type(amtydict["created_at"]))
        self.assertEqual(str, type(amtydict["updated_at"]))

    def testAmenityto_dictoutput(self):
        """test Amenity 'to_dict' output matches the expected dict"""
        currdt = datetime.today()
        amty = Amenity()
        amty.id = "246810"
        amty.created_at = amty.updated_at = currdt
        expdict = {'id': '246810', '__class__': 'Amenity',
                   'created_at': currdt.isoformat(),
                   'updated_at': currdt.isoformat()}
        self.assertDictEqual(amty.to_dict(), expdict)

    def testAmenityto_dictand__dict__(self):
        """test the output of Amenity 'to_dict' to __dict__"""
        self.assertNotEqual(Amenity().to_dict, Amenity().__dict__)

    def testAmenityto_dictargs(self):
        """test Amenity 'to_dict' with handling passed  arguments"""
        self.assertRaises(TypeError, lambda: Amenity().to_dict(None))


if __name__ == "__main__":
    unittest.main()
