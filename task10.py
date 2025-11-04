class BankAccount:
    def __init__(self, owner: str, balance: float | int):
       self.owner = owner
       self.balance = balance
    
    def deposit(self, amount: int | float):
        self.balance += amount
        print(f"balancega {amount} qoshildi!\nbalance = {self.balance}\n")
    def withdraw(self, amount: int | float):
        if amount <= self.balance:
            self.balance -= amount
            print(f"balancedan {amount} yechib olindi!\nbalance = {self.balance} qoldi\n")
        else:
            print('Balans yetarli emas')
        
men1 = BankAccount('Daler', 100_000_000)
men2 = BankAccount('Samandar', 100_000_000)

men1.deposit(100_000_000)
men1.withdraw(199_000_000)
men2.deposit(100_000_000)
men2.withdraw(200_000_000)