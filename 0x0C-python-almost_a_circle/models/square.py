#!/usr/bin/python3
"""This is the Square module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This is the Square class that inherits from Rectangle

    Args:
        Rectangle (_type_): _description_
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Square class constructor.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the top-left corner.
                Defaults to 0.
            y (int, optional): The y-coordinate of the top-left corner.
                Defaults to 0.
            id (int, optional): The identifier of the square.
                Defaults to None.
        """
        self.__width = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter method for size attribute

        Returns:
            int: size attribute
        """
        return self.__width

    @size.setter
    def size(self, value):
        """Set the value for the size

        Args:
            value (int): The new value for the size

        Raises:
            TypeError: if value is not an integer
            ValueError: if the value is less than or equal to zero
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """Update attributes using either positional arguments or
            keyword arguments.

        Args:
            *args: Positional arguments representing id, size, x, and y.
            **kwargs: Keyword arguments representing id, size, x, and y.
        """
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
        """Return a dictionary representation of the square's attributes.

        Returns:
            dict: A dictionary containing 'id', 'size', 'x', and 'y'.
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """Return a string representation of the square.

        Returns:
            str: A string in the format "[Square] (id) x/y - size".
        """
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                                                  self.x, self.y,
                                                  self.width))
