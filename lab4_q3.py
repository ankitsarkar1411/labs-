class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_id, name, stock, price):
        self.items[item_id] = {"name": name, "stock": stock, "price": price}

    def update_item(self, item_id, stock=None, price=None):
        if item_id in self.items:
            if stock is not None: self.items[item_id]["stock"] = stock
            if price is not None: self.items[item_id]["price"] = price

    def check_item_details(self, item_id):
        return self.items.get(item_id, "Item not found")

# Example usage
inv = Inventory()
inv.add_item(1, "Laptop", 10, 1000)
inv.update_item(1, stock=8)
print(inv.check_item_details(1))
