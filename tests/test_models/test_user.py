#!/usr/bin/python3
"""Unittest for user.py is defined"""
import unittest
import time
import models
from os import rename, remove
from datetime import datetime
from models.user import User


class TestUserinstance(unittest.TestCase):
    """Unittest for creating instances of the User class"""

    def testUserinstancenoargs(self):
        """test User instance with no arguments"""
        self.assertEqual(type(User()), User)

    def testUsernewinstancestorage(self):
        """test User instances are stored in objects set"""
        self.assertIn(User(), models.storage.all().values())

    def testUseridattr(self):
        """test if User 'id' attr is a public string"""
        self.assertEqual(str, type(User().id))

    def testUsercreated_atattr(self):
        """test if User 'created_at' attr is a pub datetime obj"""
        self.assertEqual(datetime, type(User().created_at))

    def testUserupdated_atattr(self):
        """test if User 'updated_at' attr is a pub datetime obj"""
        self.assertEqual(datetime, type(User().updated_at))

    def testUseremailattr(self):
        """test if User 'email' attr is a public string"""
        self.assertEqual(str, type(User.email))

    def testUserpasswordattr(self):
        """test if User 'password' attr is a public string"""
        self.assertEqual(str, type(User.password))

    def testUserfirst_nameattr(self):
        """test if User 'first_name' attr is a public string"""
        self.assertEqual(str, type(User.first_name))

    def testUserlast_nameattr(self):
        """test if User 'last_name' attr is a public string"""
        self.assertEqual(str, type(User.last_name))

    def testUsertwoids(self):
        """test that two User instances have unique 'ids'"""
        usr1 = User()
        usr2 = User()
        self.assertNotEqual(usr1.id, usr2.id)

    def testUsertwocreated_at(self):
        """test the 'created_at' timestamp of two User instances"""
        usr1 = User()
        time.sleep(0.07)
        usr2 = User()
        self.assertLess(usr1.created_at, usr2.created_at)

    def testUsertwoupdated_at(self):
        """test the 'updated_at' timestamp of two User instances"""
        usr1 = User()
        time.sleep(0.07)
        usr2 = User()
        self.assertLess(usr1.updated_at, usr2.updated_at)

    def testUserstrrep(self):
        """test the string representation of a User instance"""
        currdt = datetime.today()
        dtrepr = repr(currdt)
        usr = User()
        usr.id = "13579"
        usr.created_at = usr.updated_at = currdt
        usrstr = usr.__str__()
        self.assertIn("[User] (13579)", usrstr)
        self.assertIn("'id': '13579'", usrstr)
        self.assertIn("'created_at': " + dtrepr, usrstr)
        self.assertIn("'updated_at': " + dtrepr, usrstr)

    def testUserunusedargs(self):
        """test that unused arguments do not affect HaseModel instances"""
        self.assertNotIn(None, User(None).__dict__.values())

    def testUserinstancekwargs(self):
        """test User instantiation with specified keywordargs(kwargs)"""
        currdt = datetime.today()
        dtiso = currdt.isoformat()
        usr = User(id="246", created_at=dtiso, updated_at=dtiso)
        self.assertEqual(usr.id, "246")
        self.assertEqual(usr.created_at, currdt)
        self.assertEqual(usr.updated_at, currdt)

    def testUserinstanceNonekwargs(self):
        """test User instantiation with None as kwargs"""
        self.assertRaises(TypeError, lambda: User(id=None,
                          created_at=None, updated_at=None))


class TestUsersave(unittest.TestCase):
    """Unittest for the save method of the User class"""

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

    def testUseronesave(self):
        """test that User 'save' call updates 'updated_at' timestamp"""
        usr = User()
        time.sleep(0.08)
        fstupdated_at = usr.updated_at
        usr.save()
        self.assertLess(fstupdated_at, usr.updated_at)

    def testUsertwosaves(self):
        """test two User 'save' calls updates 'updated_at' timestamps"""
        usr = User()
        time.sleep(0.08)
        fstupdated_at = usr.updated_at
        usr.save()
        scdupdated_at = usr.updated_at
        self.assertLess(fstupdated_at, scdupdated_at)
        time.sleep(0.08)
        usr.save()
        self.assertLess(scdupdated_at, usr.updated_at)

    def testUsersaveargs(self):
        """test User 'save' call with arguments"""
        self.assertRaises(TypeError, lambda: User().save(None))

    def testUsersaveJSONfile(self):
        """test User 'save' call updates the corresponding JSON file"""
        usr = User()
        usr.save()
        usrid = "User." + usr.id
        with open("file.json", "r") as fl:
            self.assertIn(usrid, fl.read())


class TestUserto_dict(unittest.TestCase):
    """Unittest for the 'to_dict' method of the User class"""

    def testUserto_dcittype(self):
        """test User 'to_dict' output is a dictionary"""
        self.assertTrue(dict, type(User().to_dict()))

    def testUserto_dictkeys(self):
        """test User 'to_dict' dictionary contains the correct keys"""
        self.assertIn("id", User().to_dict())
        self.assertIn("created_at", User().to_dict())
        self.assertIn("updated_at", User().to_dict())
        self.assertIn("__class__", User().to_dict())

    def testBasemodelto_dictaddattr(self):
        """test that User 'to_dict' dict has additional attributes"""
        usr = User()
        usr.name = "Taiwo_and_Olamide"
        usr.number = 147
        self.assertIn("name", usr.to_dict())
        self.assertIn("number", usr.to_dict())

    def testUserto_dictdatetimeattr(self):
        """test User 'to_dict' dict datetime attr are string reps"""
        usrdict = User().to_dict()
        self.assertEqual(str, type(usrdict["created_at"]))
        self.assertEqual(str, type(usrdict["updated_at"]))

    def testUserto_dictoutput(self):
        """test User 'to_dict' output matches the expected dict"""
        currdt = datetime.today()
        usr = User()
        usr.id = "246810"
        usr.created_at = usr.updated_at = currdt
        expdict = {'id': '246810', '__class__': 'User',
                   'created_at': currdt.isoformat(),
                   'updated_at': currdt.isoformat()}
        self.assertDictEqual(usr.to_dict(), expdict)

    def testUserto_dictand__dict__(self):
        """test the output of User 'to_dict' to __dict__"""
        self.assertNotEqual(User().to_dict, User().__dict__)

    def testUserto_dictargs(self):
        """test User 'to_dict' with handling passed  arguments"""
        self.assertRaises(TypeError, lambda: User().to_dict(None))


if __name__ == "__main__":
    unittest.main()
