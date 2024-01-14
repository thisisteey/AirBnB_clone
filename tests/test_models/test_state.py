#!/usr/bin/python3
"""Unittest for state.py is defined"""
import unittest
import time
import models
from os import rename, remove
from datetime import datetime
from models.state import State


class TestStateinstance(unittest.TestCase):
    """Unittest for creating instances of the State class"""

    def testStateinstancenoargs(self):
        """test State instance with no arguments"""
        self.assertEqual(type(State()), State)

    def testStatenewinstancestorage(self):
        """test State instances are stored in objects set"""
        self.assertIn(State(), models.storage.all().values())

    def testStateidattr(self):
        """test if State 'id' attr is a public string"""
        self.assertEqual(str, type(State().id))

    def testStatecreated_atattr(self):
        """test if State 'created_at' attr is a pub datetime obj"""
        self.assertEqual(datetime, type(State().created_at))

    def testStateupdated_atattr(self):
        """test if State 'updated_at' attr is a pub datetime obj"""
        self.assertEqual(datetime, type(State().updated_at))

    def testStatenameattr(self):
        """test if State 'name' is a public class attribute"""
        self.assertEqual(str, type(State.name))
        self.assertIn("name", dir(State()))
        self.assertNotIn("name", State().__dict__)

    def testStatetwoids(self):
        """test that two State instances have unique 'ids'"""
        ste1 = State()
        ste2 = State()
        self.assertNotEqual(ste1.id, ste2.id)

    def testStatetwocreated_at(self):
        """test the 'created_at' timestamp of two State instances"""
        ste1 = State()
        time.sleep(0.07)
        ste2 = State()
        self.assertLess(ste1.created_at, ste2.created_at)

    def testStatetwoupdated_at(self):
        """test the 'updated_at' timestamp of two State instances"""
        ste1 = State()
        time.sleep(0.07)
        ste2 = State()
        self.assertLess(ste1.updated_at, ste2.updated_at)

    def testStatestrrep(self):
        """test the string representation of a State instance"""
        currdt = datetime.today()
        dtrepr = repr(currdt)
        ste = State()
        ste.id = "13579"
        ste.created_at = ste.updated_at = currdt
        stestr = ste.__str__()
        self.assertIn("[State] (13579)", stestr)
        self.assertIn("'id': '13579'", stestr)
        self.assertIn("'created_at': " + dtrepr, stestr)
        self.assertIn("'updated_at': " + dtrepr, stestr)

    def testStateunusedargs(self):
        """test that unused arguments do not affect HaseModel instances"""
        self.assertNotIn(None, State(None).__dict__.values())

    def testStateinstancekwargs(self):
        """test State instantiation with specified keywordargs(kwargs)"""
        currdt = datetime.today()
        dtiso = currdt.isoformat()
        ste = State(id="246", created_at=dtiso, updated_at=dtiso)
        self.assertEqual(ste.id, "246")
        self.assertEqual(ste.created_at, currdt)
        self.assertEqual(ste.updated_at, currdt)

    def testStateinstanceNonekwargs(self):
        """test State instantiation with None as kwargs"""
        self.assertRaises(TypeError, lambda: State(id=None,
                          created_at=None, updated_at=None))


class TestStatesave(unittest.TestCase):
    """Unittest for the save method of the State class"""

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

    def testStateonesave(self):
        """test that State 'save' call updates 'updated_at' timestamp"""
        ste = State()
        time.sleep(0.08)
        fstupdated_at = ste.updated_at
        ste.save()
        self.assertLess(fstupdated_at, ste.updated_at)

    def testStatetwosaves(self):
        """test two State 'save' calls updates 'updated_at' timestamps"""
        ste = State()
        time.sleep(0.08)
        fstupdated_at = ste.updated_at
        ste.save()
        scdupdated_at = ste.updated_at
        self.assertLess(fstupdated_at, scdupdated_at)
        time.sleep(0.08)
        ste.save()
        self.assertLess(scdupdated_at, ste.updated_at)

    def testStatesaveargs(self):
        """test State 'save' call with arguments"""
        self.assertRaises(TypeError, lambda: State().save(None))

    def testStatesaveJSONfile(self):
        """test State 'save' call updates the corresponding JSON file"""
        ste = State()
        ste.save()
        steid = "State." + ste.id
        with open("file.json", "r") as fl:
            self.assertIn(steid, fl.read())


class TestStateto_dict(unittest.TestCase):
    """Unittest for the 'to_dict' method of the State class"""

    def testStateto_dcittype(self):
        """test State 'to_dict' output is a dictionary"""
        self.assertTrue(dict, type(State().to_dict()))

    def testStateto_dictkeys(self):
        """test State 'to_dict' dictionary contains the correct keys"""
        self.assertIn("id", State().to_dict())
        self.assertIn("created_at", State().to_dict())
        self.assertIn("updated_at", State().to_dict())
        self.assertIn("__class__", State().to_dict())

    def testBasemodelto_dictaddattr(self):
        """test that State 'to_dict' dict has additional attributes"""
        ste = State()
        ste.name = "Taiwo_and_Olamide"
        ste.number = 147
        self.assertIn("name", ste.to_dict())
        self.assertIn("number", ste.to_dict())

    def testStateto_dictdatetimeattr(self):
        """test State 'to_dict' dict datetime attr are string reps"""
        stedict = State().to_dict()
        self.assertEqual(str, type(stedict["created_at"]))
        self.assertEqual(str, type(stedict["updated_at"]))

    def testStateto_dictoutput(self):
        """test State 'to_dict' output matches the expected dict"""
        currdt = datetime.today()
        ste = State()
        ste.id = "246810"
        ste.created_at = ste.updated_at = currdt
        expdict = {'id': '246810', '__class__': 'State',
                   'created_at': currdt.isoformat(),
                   'updated_at': currdt.isoformat()}
        self.assertDictEqual(ste.to_dict(), expdict)

    def testStateto_dictand__dict__(self):
        """test the output of State 'to_dict' to __dict__"""
        self.assertNotEqual(State().to_dict, State().__dict__)

    def testStateto_dictargs(self):
        """test State 'to_dict' with handling passed  arguments"""
        self.assertRaises(TypeError, lambda: State().to_dict(None))


if __name__ == "__main__":
    unittest.main()
