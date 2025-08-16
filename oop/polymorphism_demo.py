# File: oop/polymorphism_demo.py

import math

class Shape:
    """Base class representing a generic shape."""

    def area(self):
        """Method to calculate area, expected to be overridden."""
        raise NotImplementedError("Subclasses must override the area() method")


class Rectangle(Shape):
    """Rectangle shape, derived from Shape."""
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        """Calculate and return the area of a rectangle."""
        return self.length * self.width


class Circle(Shape):
    """Circle shape, derived from Shape."""
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        """Calculate and return the area of a circle."""
        return math.pi * (self.radius ** 2)
