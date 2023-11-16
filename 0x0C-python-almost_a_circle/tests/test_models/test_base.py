#!/usr/bin/python3
"""This is the test case model for Base class
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_auto_assign_id(self):
        my_instance = Base()
        my_instance1 = Base(id=26)
        
        self.assertEqual(my_instance.id, 1)
        self.assertEqual(my_instance1.id, 26)