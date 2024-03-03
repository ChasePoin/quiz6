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
    
class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def get_area(self):
        return (self.side * self.side)
    
# to add a new shape, all you have to do is create the class and inherit Shape, then add a get_area method
    
def main():
    redCircle = Circle(5)
    print(redCircle.get_area())

if __name__ == "__main__":
    main()