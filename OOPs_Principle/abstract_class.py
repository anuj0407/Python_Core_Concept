'''
Abstraction is one of the priciples of OOPs
Abstraction is the process of hiding the internal details of an object and only exposing the necessary features.
It is achieved by using abstract classes and interfaces. An abstract class is a class that cannot be instansiated and is meant to be subclassed.
It contains one or more abstract methods, which are methods that are declared but do not have an implementation.
In Python, we can create an abstract class by using the abc module and the ABC class. We can define abstract methods using the @abstractmethod decorator.
'''

from abc import ABC, abstractmethod
# abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Inheriting the abstract class and providing implementation for the abstract method
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# obj = Shape()  # This would raise a TypeError because Shape is an abstract class
cir = Circle(3)
print("Area of the circle:", cir.area())
rect = Rectangle(5, 10)
print("Area of the rectangle:", rect.area())