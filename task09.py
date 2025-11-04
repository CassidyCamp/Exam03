class Animal:
    def __init__(self, name, sound):
       self.name = name
       self.sound = sound
    
    def make_sound(self):
        return f'{self.name} says {self.sound}!'
    

n1 = Animal('dog', 'woof')
n2 = Animal('cat', 'mia')

print(n1.make_sound())
print(n2.make_sound())