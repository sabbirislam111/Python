class Device:
    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color

    def __repr__(self) -> str:
        return f'Brand {self.brand}, Price {self.price}, Color {self.color}'


class Laptop(Device):

    def __init__(self, brand, price, color, desk):
        super().__init__(brand, price, color)
        self.dock = desk

    def sart(self):
        print("Start the laptop")


class Phone(Device):

    def __init__(self, brand, price, color, sim_card):
        super().__init__(brand, price, color)
        self.sim_card = sim_card

    def sell(self, amount):
        if amount < self.price:
            print("You can't Buy ")


lenovo = Laptop('Lenovo', 20000, "Black", "1Tb")
print(lenovo)

nokia = Phone('Nokia', 12000, "red", 2)
print(nokia)


