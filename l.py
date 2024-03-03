from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def get_area(self) -> int:
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self) -> int:
        return (self.radius * self.radius * math.pi)
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def get_area(self) -> int:
        return (0.5 * self.base * self.height)
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def get_area(self) -> int:
        return (self.height * self.width)
    
# potential implementation of a "Polygon" class
class Polygon(Shape):
    def __init__(self, numSides, sideLength):
        self.numSides = numSides
        self.sideLength = sideLength
    def get_area(self) -> int:
        # implement way to calculate the area of the polygon based on the number of sides and side length, then return the area
        # this will then follow the structure of the rest of the shapes, fulfilling LSP
        return 1
    
# 1. you are able to fix the issue of Rectangle and Triangle having setters by making the instantiation of an object set them by passing in values, making each "setter"
# part of __init__
# 2. No, it is not a violation of LSP as each shape has get_area() to calculate the area of the shape and return it.
# 3. possible implementation of a Polygon class (get_area is unimplemented)
def main():
    redCircle = Circle(5)
    print(redCircle.get_area())

if __name__ == "__main__":
    main()