class Restaurant:
    def __init__(self):
        self.menu, self.tables, self.orders = {}, [], {}

    def add_item_to_menu(self, name, price): self.menu[name] = price
    def book_table(self, table_no): self.tables.append(table_no)
    def customer_order(self, table_no, item): self.orders.setdefault(table_no, []).append(item)

    def print_menu(self): print(self.menu)
    def print_tables(self): print(self.tables)
    def print_orders(self): print(self.orders)

# Example usage
r = Restaurant()
r.add_item_to_menu("Pizza", 10)
r.book_table(1)
r.customer_order(1, "Pizza")
r.print_menu(); r.print_tables(); r.print_orders()
