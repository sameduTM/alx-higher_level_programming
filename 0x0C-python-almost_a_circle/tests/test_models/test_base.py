#!/usr/bin/python3
"""This is the test case model for Base class
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_auto_assign_id(self):
        my_inst0 = Base()
        self.assertEqual(my_inst0.id, 1)
        my_inst1 = Base()
        self.assertEqual(my_inst1.id, 2)
        my_inst2 = Base()
        self.assertEqual(my_inst2.id, 3)
        Base._Base__nb_objects = 0

if __name__ == '__main__':
    unittest.main()