#!/usr/bin/python3
from models.base import Base

"""This is the Rectangle Module - imports from Base Module

Raises:
    TypeError: If width, height, x, or y is not an integer.
    ValueError: If width, height, x, or y is not greater than 0.
    TypeError: If x or y is not an integer in the display method.
    ValueError: If x or y is less than 0 in the display method.
    TypeError: If any argument in the update method is not an integer.
    ValueError: If x or y is less than 0 in the update method.
    TypeError: If any keyword argument in the update method has
    an invalid key.
    ValueError: If any keyword argument in the update method
    has an invalid value.

Returns:
    dict: A dictionary representation of the rectangle's attributes.
"""


class Rectangle(Base):
    """_summary_

    Args:
        Base (type): The base class from which Rectangle inherits.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the top-left corner.
                Defaults to 0.
            y (int, optional): The y-coordinate of the top-left corner.
                Defaults to 0.
            id (int, optional): The identifier of the rectangle.
                Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter method for width

        Returns:
            int: encapsulated width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width attribute.

        Args:
            value (int): The new value for the width.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height

        Returns:
            int: encapsulated height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height attribute.

        Args:
            value (int): The new value for the height.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter method for x-coordinate
        Returns:
            int: The x-coordinate
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x-coordinate attribute.

        Args:
            value (int): The new value for the x-coordinate.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter method for the y-coordinate

        Returns:
            int: the y-coordinate
        """
        return self.__y

    @y.setter
    def y(self, value):
        """This is the setter method of y-coordinate

        Args:
            value (int): new value for y-coordinate

        Raises:
            TypeError: value is not an integer
            ValueError: value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle (width times height).
        """
        return self.width * self.height

    def display(self):
        """Display the rectangle by printing '#' characters.
        """
        bl = "\n" * self.__y
        s = " " * self.__x
        print(bl, end="")
        for i in range(self.__height):
            print(s, end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """Update attributes using either positional
            arguments or keyword arguments.

        Args:
            *args: Positional arguments representing id, width,
                height, x, and y.
            **kwargs: Keyword arguments representing id, width,
                height, x, and y.

        Raises:
            TypeError: If any argument is not an integer.
            ValueError: If x or y is less than 0.
            TypeError: If any keyword argument has an invalid key.
            ValueError: If any keyword argument has an invalid value.
        """
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
        """Return a dictionary representation of the rectangle's attributes.

        Returns:
            dict: A dictionary containing 'id', 'width', 'height',
                'x', and 'y'.
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """Return a string representation of the rectangle.

        Returns:
            str: A string in the format "[Rectangle] (id) x/y - width/height".
        """
        return (
            f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
            f"{self.width}/{self.height}"
        )
