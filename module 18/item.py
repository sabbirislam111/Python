import json

class Item:
    all = []
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.all.append(self)

    @staticmethod
    def initialize():
        with open("extract.txt", "r") as tx:
            data = tx.read()
            js = json.loads(data)
        for item in js:
            Item(item["name"], item["price"])

    def __repr__(self) -> str:
        return f"(Item: {self.name}, {self.price})"


    
# item = Item("test", 100)
Item.initialize()
print(Item.all)

