#!/usr/bin/python3
"""Unittest for place.py is defined"""
import unittest
import time
import models
from os import rename, remove
from datetime import datetime
from models.place import Place


class TestPlaceinstance(unittest.TestCase):
    """Unittest for creating instances of the Place class"""

    def testPlaceinstancenoargs(self):
        """test Place instance with no arguments"""
        self.assertEqual(type(Place()), Place)

    def testPlacenewinstancestorage(self):
        """test Place instances are stored in objects set"""
        self.assertIn(Place(), models.storage.all().values())

    def testPlaceidattr(self):
        """test if Place 'id' attr is a public string"""
        self.assertEqual(str, type(Place().id))

    def testPlacecreated_atattr(self):
        """test if Place 'created_at' attr is a pub datetime obj"""
        self.assertEqual(datetime, type(Place().created_at))

    def testPlaceupdated_atattr(self):
        """test if Place 'updated_at' attr is a pub datetime obj"""
        self.assertEqual(datetime, type(Place().updated_at))

    def testPlacecity_idattr(self):
        """test if Place 'city_id' is a public class attribute"""
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(Place()))
        self.assertNotIn("city_id", Place().__dict__)

    def testPlaceuser_idattr(self):
        """test if Place 'user_id' is a public class attribute"""
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(Place()))
        self.assertNotIn("user_id", Place().__dict__)

    def testPlacenameattr(self):
        """test if Place 'name' is a public class attribute"""
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(Place()))
        self.assertNotIn("name", Place().__dict__)

    def testPlacedescriptionattr(self):
        """test if Place 'description' is a public class attribute"""
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(Place()))
        self.assertNotIn("description", Place().__dict__)

    def testPlacenumber_roomsattr(self):
        """test if Place 'number_rooms' is a public class attribute"""
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(Place()))
        self.assertNotIn("number_rooms", Place().__dict__)

    def testPlacenumber_bathroomsattr(self):
        """test if Place 'number_bathrooms' is a public class attribute"""
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(Place()))
        self.assertNotIn("number_bathrooms", Place().__dict__)

    def testPlacemax_guestattr(self):
        """test if Place 'max_guest' is a public class attribute"""
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(Place()))
        self.assertNotIn("max_guest", Place().__dict__)

    def testPlaceprice_by_nightattr(self):
        """test if Place 'price_by_night' is a public class attribute"""
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(Place()))
        self.assertNotIn("price_by_night", Place().__dict__)

    def testPlacelatitudeattr(self):
        """test if Place 'latitude' is a public class attribute"""
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(Place()))
        self.assertNotIn("latitude", Place().__dict__)

    def testPlacelongitudeattr(self):
        """test if Place 'longitude' is a public class attribute"""
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(Place()))
        self.assertNotIn("longitude", Place().__dict__)

    def testPlaceamenity_idsattr(self):
        """test if Place 'amenity_ids' is a public class attribute"""
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(Place()))
        self.assertNotIn("amenity_ids", Place().__dict__)

    def testPlacetwoids(self):
        """test that two Place instances have unique 'ids'"""
        plc1 = Place()
        plc2 = Place()
        self.assertNotEqual(plc1.id, plc2.id)

    def testPlacetwocreated_at(self):
        """test the 'created_at' timestamp of two Place instances"""
        plc1 = Place()
        time.sleep(0.07)
        plc2 = Place()
        self.assertLess(plc1.created_at, plc2.created_at)

    def testPlacetwoupdated_at(self):
        """test the 'updated_at' timestamp of two Place instances"""
        plc1 = Place()
        time.sleep(0.07)
        plc2 = Place()
        self.assertLess(plc1.updated_at, plc2.updated_at)

    def testPlacestrrep(self):
        """test the string representation of a Place instance"""
        currdt = datetime.today()
        dtrepr = repr(currdt)
        plc = Place()
        plc.id = "13579"
        plc.created_at = plc.updated_at = currdt
        plcstr = plc.__str__()
        self.assertIn("[Place] (13579)", plcstr)
        self.assertIn("'id': '13579'", plcstr)
        self.assertIn("'created_at': " + dtrepr, plcstr)
        self.assertIn("'updated_at': " + dtrepr, plcstr)

    def testPlaceunusedargs(self):
        """test that unused arguments do not affect HaseModel instances"""
        self.assertNotIn(None, Place(None).__dict__.values())

    def testPlaceinstancekwargs(self):
        """test Place instantiation with specified keywordargs(kwargs)"""
        currdt = datetime.today()
        dtiso = currdt.isoformat()
        plc = Place(id="246", created_at=dtiso, updated_at=dtiso)
        self.assertEqual(plc.id, "246")
        self.assertEqual(plc.created_at, currdt)
        self.assertEqual(plc.updated_at, currdt)

    def testPlaceinstanceNonekwargs(self):
        """test Place instantiation with None as kwargs"""
        self.assertRaises(TypeError, lambda: Place(id=None,
                          created_at=None, updated_at=None))


class TestPlacesave(unittest.TestCase):
    """Unittest for the save method of the Place class"""

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

    def testPlaceonesave(self):
        """test that Place 'save' call updates 'updated_at' timestamp"""
        plc = Place()
        time.sleep(0.08)
        fstupdated_at = plc.updated_at
        plc.save()
        self.assertLess(fstupdated_at, plc.updated_at)

    def testPlacetwosaves(self):
        """test two Place 'save' calls updates 'updated_at' timestamps"""
        plc = Place()
        time.sleep(0.08)
        fstupdated_at = plc.updated_at
        plc.save()
        scdupdated_at = plc.updated_at
        self.assertLess(fstupdated_at, scdupdated_at)
        time.sleep(0.08)
        plc.save()
        self.assertLess(scdupdated_at, plc.updated_at)

    def testPlacesaveargs(self):
        """test Place 'save' call with arguments"""
        self.assertRaises(TypeError, lambda: Place().save(None))

    def testPlacesaveJSONfile(self):
        """test Place 'save' call updates the corresponding JSON file"""
        plc = Place()
        plc.save()
        plcid = "Place." + plc.id
        with open("file.json", "r") as fl:
            self.assertIn(plcid, fl.read())


class TestPlaceto_dict(unittest.TestCase):
    """Unittest for the 'to_dict' method of the Place class"""

    def testPlaceto_dcittype(self):
        """test Place 'to_dict' output is a dictionary"""
        self.assertTrue(dict, type(Place().to_dict()))

    def testPlaceto_dictkeys(self):
        """test Place 'to_dict' dictionary contains the correct keys"""
        self.assertIn("id", Place().to_dict())
        self.assertIn("created_at", Place().to_dict())
        self.assertIn("updated_at", Place().to_dict())
        self.assertIn("__class__", Place().to_dict())

    def testBasemodelto_dictaddattr(self):
        """test that Place 'to_dict' dict has additional attributes"""
        plc = Place()
        plc.name = "Taiwo_and_Olamide"
        plc.number = 147
        self.assertIn("name", plc.to_dict())
        self.assertIn("number", plc.to_dict())

    def testPlaceto_dictdatetimeattr(self):
        """test Place 'to_dict' dict datetime attr are string reps"""
        plcdict = Place().to_dict()
        self.assertEqual(str, type(plcdict["created_at"]))
        self.assertEqual(str, type(plcdict["updated_at"]))

    def testPlaceto_dictoutput(self):
        """test Place 'to_dict' output matches the expected dict"""
        currdt = datetime.today()
        plc = Place()
        plc.id = "246810"
        plc.created_at = plc.updated_at = currdt
        expdict = {'id': '246810', '__class__': 'Place',
                   'created_at': currdt.isoformat(),
                   'updated_at': currdt.isoformat()}
        self.assertDictEqual(plc.to_dict(), expdict)

    def testPlaceto_dictand__dict__(self):
        """test the output of Place 'to_dict' to __dict__"""
        self.assertNotEqual(Place().to_dict, Place().__dict__)

    def testPlaceto_dictargs(self):
        """test Place 'to_dict' with handling passed  arguments"""
        self.assertRaises(TypeError, lambda: Place().to_dict(None))


if __name__ == "__main__":
    unittest.main()
