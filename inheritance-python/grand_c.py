#!/usr/bin/python3
# A Python program to demonstrate inheritance
 
# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is
# equivalent to "class Person(object)"

class Base(object):
    
    # Constructor
    def __init__(self, name):
        self.name = name
    
    # To get name
    def getName(self):
        return self.name
    
# Inherited or Sub class (Note Person in bracket)
class Child(Base):
    
    # Constructor
    def __init__(self, name, age):
        Base.__init__(self, name)
        self.age =  age
        
    # to get age
    def getAge(self):
        return self.age
    
# Inherited or Sub class (Note Person in bracket)

class GrandChild(Child):
    
    # Constructor
    def __init__(self, name, age, address):
        Child.__init__(self, name, age)
        self.address = address
        
    # to get address
    def getAddress(self):
        return self.address

# g = GrandChild("Bling5", 25, "Noida")
# print(g.getAddress(), g.getAge(), g.getName())
print(Base.__bases__)
print(Base.__mro__)