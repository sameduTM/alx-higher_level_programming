#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer
"""
This is a unittest module for max integer
"""

    
class TestMaxInteger(unittest.TestCase):
    """ This is a test case class for finding max integer"""
    def test_max_integer(self):
        """This is max test case function"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([7, 2, 3, 4]), 7)
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

if __name__ == '__main__':
    unittest.main()
