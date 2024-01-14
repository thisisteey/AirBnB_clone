#!/usr/bin/python3
"""Unittest for review.py is defined"""
import unittest
import time
import models
from os import rename, remove
from datetime import datetime
from models.review import Review


class TestReviewinstance(unittest.TestCase):
    """Unittest for creating instances of the Review class"""

    def testReviewinstancenoargs(self):
        """test Review instance with no arguments"""
        self.assertEqual(type(Review()), Review)

    def testReviewnewinstancestorage(self):
        """test Review instances are stored in objects set"""
        self.assertIn(Review(), models.storage.all().values())

    def testReviewidattr(self):
        """test if Review 'id' attr is a public string"""
        self.assertEqual(str, type(Review().id))

    def testReviewcreated_atattr(self):
        """test if Review 'created_at' attr is a pub datetime obj"""
        self.assertEqual(datetime, type(Review().created_at))

    def testReviewupdated_atattr(self):
        """test if Review 'updated_at' attr is a pub datetime obj"""
        self.assertEqual(datetime, type(Review().updated_at))

    def testReviewplace_idattr(self):
        """test if Review 'place_id' is a public class attribute"""
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(Review()))
        self.assertNotIn("place_id", Review().__dict__)

    def testReviewuser_idattr(self):
        """test if Review 'user_id' is a public class attribute"""
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(Review()))
        self.assertNotIn("user_id", Review().__dict__)

    def testReviewtextattr(self):
        """test if Review 'text' is a public class attribute"""
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(Review()))
        self.assertNotIn("text", Review().__dict__)

    def testReviewtwoids(self):
        """test that two Review instances have unique 'ids'"""
        rev1 = Review()
        rev2 = Review()
        self.assertNotEqual(rev1.id, rev2.id)

    def testReviewtwocreated_at(self):
        """test the 'created_at' timestamp of two Review instances"""
        rev1 = Review()
        time.sleep(0.07)
        rev2 = Review()
        self.assertLess(rev1.created_at, rev2.created_at)

    def testReviewtwoupdated_at(self):
        """test the 'updated_at' timestamp of two Review instances"""
        rev1 = Review()
        time.sleep(0.07)
        rev2 = Review()
        self.assertLess(rev1.updated_at, rev2.updated_at)

    def testReviewstrrep(self):
        """test the string representation of a Review instance"""
        currdt = datetime.today()
        dtrepr = repr(currdt)
        rev = Review()
        rev.id = "13579"
        rev.created_at = rev.updated_at = currdt
        revstr = rev.__str__()
        self.assertIn("[Review] (13579)", revstr)
        self.assertIn("'id': '13579'", revstr)
        self.assertIn("'created_at': " + dtrepr, revstr)
        self.assertIn("'updated_at': " + dtrepr, revstr)

    def testReviewunusedargs(self):
        """test that unused arguments do not affect HaseModel instances"""
        self.assertNotIn(None, Review(None).__dict__.values())

    def testReviewinstancekwargs(self):
        """test Review instantiation with specified keywordargs(kwargs)"""
        currdt = datetime.today()
        dtiso = currdt.isoformat()
        rev = Review(id="246", created_at=dtiso, updated_at=dtiso)
        self.assertEqual(rev.id, "246")
        self.assertEqual(rev.created_at, currdt)
        self.assertEqual(rev.updated_at, currdt)

    def testReviewinstanceNonekwargs(self):
        """test Review instantiation with None as kwargs"""
        self.assertRaises(TypeError, lambda: Review(id=None,
                          created_at=None, updated_at=None))


class TestReviewsave(unittest.TestCase):
    """Unittest for the save method of the Review class"""

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

    def testReviewonesave(self):
        """test that Review 'save' call updates 'updated_at' timestamp"""
        rev = Review()
        time.sleep(0.08)
        fstupdated_at = rev.updated_at
        rev.save()
        self.assertLess(fstupdated_at, rev.updated_at)

    def testReviewtwosaves(self):
        """test two Review 'save' calls updates 'updated_at' timestamps"""
        rev = Review()
        time.sleep(0.08)
        fstupdated_at = rev.updated_at
        rev.save()
        scdupdated_at = rev.updated_at
        self.assertLess(fstupdated_at, scdupdated_at)
        time.sleep(0.08)
        rev.save()
        self.assertLess(scdupdated_at, rev.updated_at)

    def testReviewsaveargs(self):
        """test Review 'save' call with arguments"""
        self.assertRaises(TypeError, lambda: Review().save(None))

    def testReviewsaveJSONfile(self):
        """test Review 'save' call updates the corresponding JSON file"""
        rev = Review()
        rev.save()
        revid = "Review." + rev.id
        with open("file.json", "r") as fl:
            self.assertIn(revid, fl.read())


class TestReviewto_dict(unittest.TestCase):
    """Unittest for the 'to_dict' method of the Review class"""

    def testReviewto_dcittype(self):
        """test Review 'to_dict' output is a dictionary"""
        self.assertTrue(dict, type(Review().to_dict()))

    def testReviewto_dictkeys(self):
        """test Review 'to_dict' dictionary contains the correct keys"""
        self.assertIn("id", Review().to_dict())
        self.assertIn("created_at", Review().to_dict())
        self.assertIn("updated_at", Review().to_dict())
        self.assertIn("__class__", Review().to_dict())

    def testBasemodelto_dictaddattr(self):
        """test that Review 'to_dict' dict has additional attributes"""
        rev = Review()
        rev.name = "Taiwo_and_Olamide"
        rev.number = 147
        self.assertIn("name", rev.to_dict())
        self.assertIn("number", rev.to_dict())

    def testReviewto_dictdatetimeattr(self):
        """test Review 'to_dict' dict datetime attr are string reps"""
        revdict = Review().to_dict()
        self.assertEqual(str, type(revdict["created_at"]))
        self.assertEqual(str, type(revdict["updated_at"]))

    def testReviewto_dictoutput(self):
        """test Review 'to_dict' output matches the expected dict"""
        currdt = datetime.today()
        rev = Review()
        rev.id = "246810"
        rev.created_at = rev.updated_at = currdt
        expdict = {'id': '246810', '__class__': 'Review',
                   'created_at': currdt.isoformat(),
                   'updated_at': currdt.isoformat()}
        self.assertDictEqual(rev.to_dict(), expdict)

    def testReviewto_dictand__dict__(self):
        """test the output of Review 'to_dict' to __dict__"""
        self.assertNotEqual(Review().to_dict, Review().__dict__)

    def testReviewto_dictargs(self):
        """test Review 'to_dict' with handling passed  arguments"""
        self.assertRaises(TypeError, lambda: Review().to_dict(None))


if __name__ == "__main__":
    unittest.main()
