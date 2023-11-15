#!/usr/bin/python3
from models.base import Base

"""This is the rectangle module"""


class Rectangle(Base):
    """This is the Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    """
    def validate(self, attr, value):
        if not isinstance(value, int):
            raise TypeError(f"{attr} must be an integer")
        elif attr in {"width", "height"} and value <= 0:
            raise ValueError(f"{attr} must be > 0")
        elif attr in {"x", "y"} and value < 0:
            raise ValueError(f"{attr} must be >= 0")
        setattr(self, f"__{attr}", value)
    """

    def area(self):
        return self.width * self.height

    def display(self):
        bl = "\n" * self.__y
        s = " " * self.__x
        print(bl, end="")
        for i in range(self.__height):
            print(s, end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        if args and len(args) > 0:
            i = 0
            for ac in args:
                if i == 0:
                    if ac is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    self.id = ac
                elif i == 1:
                    self.width = ac
                elif i == 2:
                    self.height = ac
                elif i == 3:
                    self.x = ac
                elif i == 4:
                    self.y = ac
                i += 1
        elif kwargs and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == 'id':
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        return (
            f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
            f"{self.width}/{self.height}"
        )
