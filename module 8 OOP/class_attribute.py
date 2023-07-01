
class Shop:
    cart = []

    def __init__(self, buyer):
        self.buyer = buyer

    def add_to_cart(self, item):
        self.cart.append(item)

shoper_1 = Shop("Sabbir")
shoper_1.add_to_cart("Tshirt")
print(shoper_1.cart)

shoper_2 = Shop("Sadia")
shoper_2.add_to_cart("Shoes")
print(shoper_2.cart)

