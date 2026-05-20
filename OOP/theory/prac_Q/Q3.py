# Create class FoodOrder with item name, quantity, price. Add method to calculate bill.

class FoodOrder:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def bill(self):
        print("Total bill for the item name: ", self.name , " is:", self.quantity * self.price, "for", self.quantity, "piece in quantity.")

item = FoodOrder("Pizza", 5, 650)
item.bill()