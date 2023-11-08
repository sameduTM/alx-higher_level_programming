#!/usr/bin/python3
"""Working of multiple inheritance"""

class Base1(object):
    def __init__(self):
        self.str1 = "Kimbo"
        print("Base1")

class Base2(object):
    def __init__(self):
        self.str2 = "Juja"
        print("Base2")

class Derived(Base1, Base2):
    def __init__(self):
        """Calling constructors of Base1 and Base2"""
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")
        
    def printStrs(self):
        print(self.str1, self.str2)

ob = Derived()
ob.printStrs()