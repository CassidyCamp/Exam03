class Vehicle:
    def __init__(self, brand, model):
       self.brand = brand
       self.model = model
       
    def move(self):
        return "Vehicle is moving"
    
class Car(Vehicle):
    def move(self):
        return "Car is driving"
    
v1 = Vehicle("Honda", "SuperBike")
print(v1.move())

c1 = Car("Chevrolet", "Malibu")
print(c1.move())