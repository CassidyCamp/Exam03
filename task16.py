class Bird:
    def __init__(self, ):
       pass
    
    def speak(self):
        return 'chip'

class Dog:
    def __init__(self, ):
       pass
    
    def speak(self):
        return 'woof'

b1 = Bird()
d1 = Dog()
b2 = Bird()
d2 = Dog()

animals = [b1, d1, b2, d2]

for animal in animals:
    print(animal.speak())