class Person: 
    def __init__(self, name, age):
       self.name = name
       self.age = age
    
    def introduce(self):
        return f'meni ismim {self.name} men dasturchi man'

class Student(Person):
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age 
        self.grade = grade
    
    def introduce(self):
        return f'meni ismim {self.name} men talaba man '
        
    
p1 = Person("Ali", 25)
print(p1.introduce())

s1 = Student("Hasan", 20, 2)
print(s1.introduce())