
class Shopper:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        self.cart.append({'item': item, 'price': price, 'quantity': quantity})

    def checkout(self,amount):
        price = 0
        for itm in self.cart:
            print(itm)
            price += itm['price'] * itm['quantity']
        if price > amount: 
            print(f"You don't have enough money please add { price- amount }")
        elif price < amount:
            print(f"You  have enough money your changes is { amount- price }")
        else:
            print(f"Take your product")

shopping = Shopper("Sabbir")
shopping.add_to_cart("Tshirt", 450, 3)
shopping.add_to_cart("shoes", 850, 3)
shopping.add_to_cart("pant", 650, 3)

shopping.checkout(6050)
