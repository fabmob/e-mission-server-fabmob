import unittest
from get_database import get_section_db
from utils.useful_queries import get_all_sections, get_trip_before, get_all_sections_for_user_day
from datetime import datetime

class UsefulQueriesTests(unittest.TestCase):
    def setUp(self):
        get_section_db().remove({"_id": "foo_1"})
        get_section_db().remove({"_id": "foo_2"})
        get_section_db().remove({"_id": "foo_3"})

    def tearDown(self):
        get_section_db().remove({"_id": "foo_1"})
        get_section_db().remove({"_id": "foo_2"})
        get_section_db().remove({"_id": "foo_3"})

    def testGetAllSections(self):
        get_section_db().insert({"_id": "foo_1", "trip_id": "bar"})
        get_section_db().insert({"_id": "foo_2", "trip_id": "bar"})
        get_section_db().insert({"_id": "foo_3", "trip_id": "baz"})
        self.assertEqual(len(get_all_sections("foo_1")), 2)

    def testGetAllSectionsForUserDay(self):
        dt1 = datetime(2015, 1, 1, 1, 1, 1)
        dt2 = datetime(2015, 1, 1, 2, 1, 1)
        dt3 = datetime(2015, 1, 1, 3, 1, 1)
        get_section_db().insert({"_id": "foo_1",
            "type":"move",
            "section_id": 3,
            "section_start_datetime": dt1,
            "section_end_datetime": dt2})
        get_section_db().insert({"_id": "foo_2",
            "type":"place",
            "section_start_datetime": dt2,
            "section_end_datetime": dt3})
        get_section_db().insert({"_id": "foo_3",
            "type": "move",
            "section_id": 0,
            "section_start_datetime": dt3})
        self.assertEqual(get_trip_before("foo_3")["_id"], "foo_1")


    def testGetTripBefore(self):
        dt1 = datetime(2015, 1, 1, 1, 1, 1)
        dt2 = datetime(2015, 1, 1, 2, 1, 1)
        dt3 = datetime(2015, 1, 2, 3, 1, 1)
        get_section_db().insert({"_id": "foo_1",
            "user_id": "test_user",
            "type":"move",
            "section_id": 3,
            "section_start_datetime": dt1,
            "section_end_datetime": dt2})
        get_section_db().insert({"_id": "foo_2",
            "user_id": "test_user",
            "type":"place",
            "section_start_datetime": dt2,
            "section_end_datetime": dt3})
        get_section_db().insert({"_id": "foo_3",
            "user_id": "test_user",
            "type": "move",
            "section_id": 0,
            "section_start_datetime": dt3})
        secList = get_all_sections_for_user_day("test_user", 2015, 1, 1)
        self.assertEqual(len(secList), 1)
        self.assertEqual(secList[0]._id, "foo_1")

if __name__ == '__main__':
    unittest.main()
