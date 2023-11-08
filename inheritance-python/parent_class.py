#!/usr/bin/python3
""" A python program to demo inheritance"""
class Person(object):
    
    """ Constructor """
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
    """To check if person is an Employee"""
    def Display(self):
        print(self.name, self.id)
        
"""Creating a child class"""
class Emp(Person):

    def Print(self):
        print("Emp class called")

Emp_details = Emp("Boerbill", 103)

"""calling parent class function"""
Emp_details.Display()

"""Calling child class function"""
Emp_details.Print()      