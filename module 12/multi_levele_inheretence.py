
class Vehicle:

    def __init__(self, name, license, price):
        self.name  = name
        self.license = license
        self.price = price

    

class Bus(Vehicle):
    def __init__(self, name, license, price, seat, ticket_price):
        self.seat = seat
        self.ticket_price = ticket_price
        super().__init__(name, license, price)

class ACBus(Bus):
    def __init__(self):
        super().__init__("AC Bus", "DGR357", 1400000, 52, 450)

class MiniBus(Bus):
    def __init__(self, name, license, price, seat, ticket_price):
        pass


acBus = ACBus()

print(acBus.seat)
