class Rectangle:
    def __init__(self, width, height):
       self.width = width
       self.height = height
       
    def area(self):
        return self.width * self.height
    

num1 = Rectangle(2, 10)
num2 = Rectangle(2, 10)

print(num1.area())
print(num2.area())