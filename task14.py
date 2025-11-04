class Calculator:
    def __init__(self):
       pass
    
    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Bo‘lishda xatolik"
        
calc = Calculator()
print(calc.divide(10, 2))
print(calc.divide(5, 0))  