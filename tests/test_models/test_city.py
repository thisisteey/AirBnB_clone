#!/usr/bin/python3
"""Unittest for city.py is defined"""
import unittest
import time
import models
from os import rename, remove
from datetime import datetime
from models.city import City


class TestCityinstance(unittest.TestCase):
    """Unittest for creating instances of the City class"""

    def testCityinstancenoargs(self):
        """test City instance with no arguments"""
        self.assertEqual(type(City()), City)

    def testCitynewinstancestorage(self):
        """test City instances are stored in objects set"""
        self.assertIn(City(), models.storage.all().values())

    def testCityidattr(self):
        """test if City 'id' attr is a public string"""
        self.assertEqual(str, type(City().id))

    def testCitycreated_atattr(self):
        """test if City 'created_at' attr is a pub datetime obj"""
        self.assertEqual(datetime, type(City().created_at))

    def testCityupdated_atattr(self):
        """test if City 'updated_at' attr is a pub datetime obj"""
        self.assertEqual(datetime, type(City().updated_at))

    def testCitystate_idattr(self):
        """test if City 'state_id' is a public class attribute"""
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(City()))
        self.assertNotIn("state_id", City().__dict__)

    def testCitynameattr(self):
        """test if City 'name' is a public class attribute"""
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(City()))
        self.assertNotIn("name", City().__dict__)

    def testCitytwoids(self):
        """test that two City instances have unique 'ids'"""
        cty1 = City()
        cty2 = City()
        self.assertNotEqual(cty1.id, cty2.id)

    def testCitytwocreated_at(self):
        """test the 'created_at' timestamp of two City instances"""
        cty1 = City()
        time.sleep(0.07)
        cty2 = City()
        self.assertLess(cty1.created_at, cty2.created_at)

    def testCitytwoupdated_at(self):
        """test the 'updated_at' timestamp of two City instances"""
        cty1 = City()
        time.sleep(0.07)
        cty2 = City()
        self.assertLess(cty1.updated_at, cty2.updated_at)

    def testCitystrrep(self):
        """test the string representation of a City instance"""
        currdt = datetime.today()
        dtrepr = repr(currdt)
        cty = City()
        cty.id = "13579"
        cty.created_at = cty.updated_at = currdt
        ctystr = cty.__str__()
        self.assertIn("[City] (13579)", ctystr)
        self.assertIn("'id': '13579'", ctystr)
        self.assertIn("'created_at': " + dtrepr, ctystr)
        self.assertIn("'updated_at': " + dtrepr, ctystr)

    def testCityunusedargs(self):
        """test that unused arguments do not affect HaseModel instances"""
        self.assertNotIn(None, City(None).__dict__.values())

    def testCityinstancekwargs(self):
        """test City instantiation with specified keywordargs(kwargs)"""
        currdt = datetime.today()
        dtiso = currdt.isoformat()
        cty = City(id="246", created_at=dtiso, updated_at=dtiso)
        self.assertEqual(cty.id, "246")
        self.assertEqual(cty.created_at, currdt)
        self.assertEqual(cty.updated_at, currdt)

    def testCityinstanceNonekwargs(self):
        """test City instantiation with None as kwargs"""
        self.assertRaises(TypeError, lambda: City(id=None,
                          created_at=None, updated_at=None))


class TestCitysave(unittest.TestCase):
    """Unittest for the save method of the City class"""

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

    def testCityonesave(self):
        """test that City 'save' call updates 'updated_at' timestamp"""
        cty = City()
        time.sleep(0.08)
        fstupdated_at = cty.updated_at
        cty.save()
        self.assertLess(fstupdated_at, cty.updated_at)

    def testCitytwosaves(self):
        """test two City 'save' calls updates 'updated_at' timestamps"""
        cty = City()
        time.sleep(0.08)
        fstupdated_at = cty.updated_at
        cty.save()
        scdupdated_at = cty.updated_at
        self.assertLess(fstupdated_at, scdupdated_at)
        time.sleep(0.08)
        cty.save()
        self.assertLess(scdupdated_at, cty.updated_at)

    def testCitysaveargs(self):
        """test City 'save' call with arguments"""
        self.assertRaises(TypeError, lambda: City().save(None))

    def testCitysaveJSONfile(self):
        """test City 'save' call updates the corresponding JSON file"""
        cty = City()
        cty.save()
        ctyid = "City." + cty.id
        with open("file.json", "r") as fl:
            self.assertIn(ctyid, fl.read())


class TestCityto_dict(unittest.TestCase):
    """Unittest for the 'to_dict' method of the City class"""

    def testCityto_dcittype(self):
        """test City 'to_dict' output is a dictionary"""
        self.assertTrue(dict, type(City().to_dict()))

    def testCityto_dictkeys(self):
        """test City 'to_dict' dictionary contains the correct keys"""
        self.assertIn("id", City().to_dict())
        self.assertIn("created_at", City().to_dict())
        self.assertIn("updated_at", City().to_dict())
        self.assertIn("__class__", City().to_dict())

    def testBasemodelto_dictaddattr(self):
        """test that City 'to_dict' dict has additional attributes"""
        cty = City()
        cty.name = "Taiwo_and_Olamide"
        cty.number = 147
        self.assertIn("name", cty.to_dict())
        self.assertIn("number", cty.to_dict())

    def testCityto_dictdatetimeattr(self):
        """test City 'to_dict' dict datetime attr are string reps"""
        ctydict = City().to_dict()
        self.assertEqual(str, type(ctydict["created_at"]))
        self.assertEqual(str, type(ctydict["updated_at"]))

    def testCityto_dictoutput(self):
        """test City 'to_dict' output matches the expected dict"""
        currdt = datetime.today()
        cty = City()
        cty.id = "246810"
        cty.created_at = cty.updated_at = currdt
        expdict = {'id': '246810', '__class__': 'City',
                   'created_at': currdt.isoformat(),
                   'updated_at': currdt.isoformat()}
        self.assertDictEqual(cty.to_dict(), expdict)

    def testCityto_dictand__dict__(self):
        """test the output of City 'to_dict' to __dict__"""
        self.assertNotEqual(City().to_dict, City().__dict__)

    def testCityto_dictargs(self):
        """test City 'to_dict' with handling passed  arguments"""
        self.assertRaises(TypeError, lambda: City().to_dict(None))


if __name__ == "__main__":
    unittest.main()
