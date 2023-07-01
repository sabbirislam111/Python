class Accoutn:
    def __init__(self, holder, inetial_balance):
        self.holder = holder  # Public attribute
        self.__balance = inetial_balance # Private attribute
        self._accoutn_number = 567  #protected attribute

    def deposit(self,amount):
        print(f'Adding {amount} in your account')
        self.__balance += amount
    
    def withdraw(self,amount):
        print(f'Withdraw {amount} from your account')
        self.__balance -= amount

    def accoutn_number(self):
        return self._accoutn_number


class SchoolAccount(Accoutn):
    def __init__(self, holder, inetial_balance, school):
        self.school = school
        super().__init__(holder, inetial_balance)

   

rafsan = SchoolAccount("Rafsan", 50000, "SN high school")
# print(rafsan.__balance)

rafsan.deposit(3000)
# print(rafsan.__balance)

rafsan.withdraw(40000)
# print(rafsan.__balance)
print(rafsan._accoutn_number)

print(rafsan.accoutn_number())

