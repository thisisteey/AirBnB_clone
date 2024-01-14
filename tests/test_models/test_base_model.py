#!/usr/bin/python3
"""Unittest for base_model.py is defined"""
import unittest
import time
import models
from os import rename, remove
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModelinstance(unittest.TestCase):
    """Unittest for creating instances of the BaseModel class"""

    def testBaseModelinstancenoargs(self):
        """test BaseModel instance with no arguments"""
        self.assertEqual(type(BaseModel()), BaseModel)

    def testBaseModelnewinstancestorage(self):
        """test BaseModel instances are stored in objects set"""
        self.assertIn(BaseModel(), models.storage.all().values())

    def testBaseModelidattr(self):
        """test if BaseModel 'id' attr is a public string"""
        self.assertEqual(str, type(BaseModel().id))

    def testBaseModelcreated_atattr(self):
        """test if BaseModel 'created_at' attr is a pub datetime obj"""
        self.assertEqual(datetime, type(BaseModel().created_at))

    def testBaseModelupdated_atattr(self):
        """test if BaseModel 'updated_at' attr is a pub datetime obj"""
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def testBaseModeltwoids(self):
        """test that two BaseModel instances have unique 'ids'"""
        bsm1 = BaseModel()
        bsm2 = BaseModel()
        self.assertNotEqual(bsm1.id, bsm2.id)

    def testBaseModeltwocreated_at(self):
        """test the 'created_at' timestamp of two BaseModel instances"""
        bsm1 = BaseModel()
        time.sleep(0.07)
        bsm2 = BaseModel()
        self.assertLess(bsm1.created_at, bsm2.created_at)

    def testBaseModeltwoupdated_at(self):
        """test the 'updated_at' timestamp of two BaseModel instances"""
        bsm1 = BaseModel()
        time.sleep(0.07)
        bsm2 = BaseModel()
        self.assertLess(bsm1.updated_at, bsm2.updated_at)

    def testBaseModelstrrep(self):
        """test the string representation of a BaseModel instance"""
        currdt = datetime.today()
        dtrepr = repr(currdt)
        bsm = BaseModel()
        bsm.id = "13579"
        bsm.created_at = bsm.updated_at = currdt
        bsmstr = bsm.__str__()
        self.assertIn("[BaseModel] (13579)", bsmstr)
        self.assertIn("'id': '13579'", bsmstr)
        self.assertIn("'created_at': " + dtrepr, bsmstr)
        self.assertIn("'updated_at': " + dtrepr, bsmstr)

    def testBaseModelunusedargs(self):
        """test that unused arguments do not affect HaseModel instances"""
        self.assertNotIn(None, BaseModel(None).__dict__.values())

    def testBaseModelinstancekwargs(self):
        """test BaseModel instantiation with specified keywordargs(kwargs)"""
        currdt = datetime.today()
        dtiso = currdt.isoformat()
        bsm = BaseModel(id="246", created_at=dtiso, updated_at=dtiso)
        self.assertEqual(bsm.id, "246")
        self.assertEqual(bsm.created_at, currdt)
        self.assertEqual(bsm.updated_at, currdt)

    def testBaseModelinstanceNonekwargs(self):
        """test BaseModel instantiation with None as kwargs"""
        self.assertRaises(TypeError, lambda: BaseModel(id=None,
                          created_at=None, updated_at=None))

    def testBaseModelinstanceargskwargs(self):
        """test BaseModel instantiation with positional args and kwargs"""
        currdt = datetime.today()
        dtiso = currdt.isoformat()
        bsm = BaseModel("26", id="135", created_at=dtiso, updated_at=dtiso)
        self.assertEqual(bsm.id, "135")
        self.assertEqual(bsm.created_at, currdt)
        self.assertEqual(bsm.updated_at, currdt)


class TestBaseModelsave(unittest.TestCase):
    """Unittest for the save method of the BaseModel class"""

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

    def testBaseModelonesave(self):
        """test that BaseModel 'save' call updates 'updated_at' timestamp"""
        bsm = BaseModel()
        time.sleep(0.08)
        fstupdated_at = bsm.updated_at
        bsm.save()
        self.assertLess(fstupdated_at, bsm.updated_at)

    def testBaseModeltwosaves(self):
        """test two BaseModel 'save' calls updates 'updated_at' timestamps"""
        bsm = BaseModel()
        time.sleep(0.08)
        fstupdated_at = bsm.updated_at
        bsm.save()
        scdupdated_at = bsm.updated_at
        self.assertLess(fstupdated_at, scdupdated_at)
        time.sleep(0.08)
        bsm.save()
        self.assertLess(scdupdated_at, bsm.updated_at)

    def testBaseModelsaveargs(self):
        """test BaseModel 'save' call with arguments"""
        self.assertRaises(TypeError, lambda: BaseModel().save(None))

    def testBaseModelsaveJSONfile(self):
        """test BaseModel 'save' call updates the corresponding JSON file"""
        bsm = BaseModel()
        bsm.save()
        bsmid = "BaseModel." + bsm.id
        with open("file.json", "r") as fl:
            self.assertIn(bsmid, fl.read())


class TestBaseModelto_dict(unittest.TestCase):
    """Unittest for the 'to_dict' method of the BaseModel class"""

    def testBaseModelto_dcittype(self):
        """test BaseModel 'to_dict' output is a dictionary"""
        self.assertTrue(dict, type(BaseModel().to_dict()))

    def testBaseModelto_dictkeys(self):
        """test BaseModel 'to_dict' dictionary contains the correct keys"""
        self.assertIn("id", BaseModel().to_dict())
        self.assertIn("created_at", BaseModel().to_dict())
        self.assertIn("updated_at", BaseModel().to_dict())
        self.assertIn("__class__", BaseModel().to_dict())

    def testBasemodelto_dictaddattr(self):
        """test that BaseModel 'to_dict' dict has additional attributes"""
        bsm = BaseModel()
        bsm.name = "Taiwo_and_Olamide"
        bsm.number = 147
        self.assertIn("name", bsm.to_dict())
        self.assertIn("number", bsm.to_dict())

    def testBaseModelto_dictdatetimeattr(self):
        """test BaseModel 'to_dict' dict datetime attr are string reps"""
        bsmdict = BaseModel().to_dict()
        self.assertEqual(str, type(bsmdict["created_at"]))
        self.assertEqual(str, type(bsmdict["updated_at"]))

    def testBaseModelto_dictoutput(self):
        """test BaseModel 'to_dict' output matches the expected dict"""
        currdt = datetime.today()
        bsm = BaseModel()
        bsm.id = "246810"
        bsm.created_at = bsm.updated_at = currdt
        expdict = {'id': '246810', '__class__': 'BaseModel',
                   'created_at': currdt.isoformat(),
                   'updated_at': currdt.isoformat()}
        self.assertDictEqual(bsm.to_dict(), expdict)

    def testBaseModelto_dictand__dict__(self):
        """test the output of BaseModel 'to_dict' to __dict__"""
        self.assertNotEqual(BaseModel().to_dict, BaseModel().__dict__)

    def testBaseModelto_dictargs(self):
        """test BaseModel 'to_dict' with handling passed  arguments"""
        self.assertRaises(TypeError, lambda: BaseModel().to_dict(None))


if __name__ == "__main__":
    unittest.main()
