#!/usr/bin/python3
"""Parent Class"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(self.name, self.age)
    
class Student(Person):
    def __init__(self, name, age, dob):
        self.sName = name
        self.sAge = age
        self.dob = dob


        """inheriting the properties of parent class"""
        super().__init__("Honkrm", age)
        
    def displayInfo(self):
        print(self.sName, self.sAge, self.dob)
        
obj = Student("Samedu", 24, "23-12-1997")
obj.display()
obj.displayInfo()