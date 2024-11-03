class Shapes:
    
    def calc_area(self):
        return "Area"
    
    def calc_perimeter(self):
        return "Perimeter"
    
class Circle(Shapes):
    pi = 3.141592654
    def __init__(self, radius):
        self.radius = radius
        
    def calc_area(self):
        return Circle.pi * (self.radius)**2
    
class Triangle(Shapes):
    def __init__(self, base, height, side_1, side_2):
        self.base = base
        self.height = height
        self.side_1 = side_1
        self.side_2 = side_2
        
    def calc_area(self):
        return (0.5)*self.base*self.height
    
    def calc_perimeter(self):
        return self.base + self.side_1 + self.side_2
    
class Square(Shapes):
    def __init__(self, side):
        self.side = side
        
    def calc_area(self):
        return self.side**2
    
    def calc_perimeter(self):
        return 4*self.side
    
circle = Circle(34)
triangle = Triangle(12, 8, 11, 7)
square = Square(5)
print(circle.calc_area())
print(triangle.calc_perimeter())
print(triangle.calc_area())
print(triangle.calc_perimeter())
print(square.calc_area())
print(square.calc_perimeter())


