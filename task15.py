class Phone:
    def __init__(self, brand, model):
       self.brand = brand
       self.model = model
    
    def show_info(self):
        return f"Phone: {self.brand} {self.model}"


phone = Phone("Samsung", "Galaxy S21")
print(phone.show_info())