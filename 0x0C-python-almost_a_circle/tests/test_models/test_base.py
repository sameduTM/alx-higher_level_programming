#!/usr/bin/python3
"""This is the test case model for Base class
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_id(self):
        id1 = 1
        id2 = None
        id3 = 0
        
        my_instance = Base(id1)
        my_instance2 = Base(id2)
        
        self.assertEqual(my_instance.id, id1)
        self.assertEqual(my_instance2.id, id3 + 1)
        
 
if __name__=='__main__':
	unittest.main()