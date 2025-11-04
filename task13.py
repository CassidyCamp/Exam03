class Shape:
    def __init__(self):
        pass
    
    def area(self):
        pass  

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

r1 = Rectangle(2, 14)
c1 = Circle(7)
r2 = Rectangle(3, 4)
c2 = Circle(2)

shapes = [r1, c1, r2, c2]

for shape in shapes:
    print(shape.area())
