class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 10000

    def get_balance(self):
        return self.balance
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount < self.min_withdraw:
            print(f"You can't withdraw less than {self.min_withdraw}")
        elif amount > self.max_withdraw:
            print(f"You can't withdraw more than {self.max_withdraw}")
        elif amount > self.balance:
            print(f"You can't withdraw more than {self.balance}. Your current Balance is {self.balance}" )
        else :
            self.balance = self.balance - amount

    
my_accout = Bank(7000)
print(my_accout.get_balance())
my_accout.withdraw(5000)
my_accout.deposit(10000)
print(my_accout.get_balance())