from abc import ABC, abstractmethod

class IDrawable(ABC):
    @abstractmethod
    def draw(self):
        pass

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape, IDrawable):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return 3.14 * self.radius * self.radius
    
    def draw(self):
        print(f"Drawing a circle with radius {self.radius}")

class Square(Shape, IDrawable):
    def __init__(self, side):
        self.side = side
    
    def calculate_area(self):
        return self.side * self.side
    
    def draw(self):
        print(f"Drawing a square with side {self.side}")

class Triangle(Shape, IDrawable):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def calculate_area(self):
        return 0.5 * self.base * self.height
    
    def draw(self):
        print(f"Drawing a triangle with base {self.base} and height {self.height}")

def main():
    shapes = [
        Circle(5),
        Square(4),
        Triangle(3, 6)
    ]
    
    for shape in shapes:
        area = shape.calculate_area()
        shape.draw()
        print(f"Area: {area}")
        print()

if __name__ == "__main__":
    main()
