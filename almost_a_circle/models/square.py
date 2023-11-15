#!/usr/bin/python3
from models.rectangle import Rectangle
"""This is the Square module
"""


class Square(Rectangle):
    """This is the Square class that inherits from Rectangle

    Args:
        Rectangle (_type_): _description_
    """

    def __init__(self, size, x=0, y=0, id=None):
        self.__width = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.__width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if args and len(args) > 0:
            i = 0
            for ac in args:
                if i == 0:
                    if ac is None:
                        self.__init__(self.id, self.size, self.x, self.y)
                    else:
                        self.id = ac
                elif i == 1:
                    self.size = ac
                elif i == 2:
                    self.x = ac
                elif i == 3:
                    self.y = ac
                i += 1
        elif kwargs and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == 'id':
                    if value is None:
                        self.__init__(self.id, self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                                                  self.x, self.y,
                                                  self.width))
