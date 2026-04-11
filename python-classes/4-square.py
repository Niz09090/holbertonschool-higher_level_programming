#!/usr/bin/python3
"""Module that defines a Square class with a size property and validation."""


class Square:
    """A class that defines a square with a managed and validated size."""

    def __init__(self, size=0):
        """Initialize a Square instance with an optional integer size.

        Args:
            size (int): The size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with type and value validation.

        Args:
            value (int): The new size value to assign.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the current area of the square.

        Returns:
            int: The area of the square computed as size squared.
        """
        return self.__size ** 2
