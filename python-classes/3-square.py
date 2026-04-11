#!/usr/bin/python3
"""Module that defines a Square class with size validation and area method."""


class Square:
    """A class that defines a square and validates its size."""

    def __init__(self, size=0):
        """Initialize a Square instance with an optional integer size.

        Args:
            size (int): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate and return the current area of the square.

        Returns:
            int: The area of the square computed as size squared.
        """
        return self.__size ** 2
