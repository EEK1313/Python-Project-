class Product:
    def __init__(self, product_id, name, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity

    def display_info(self):
        return f"ID: {self.product_id} | Product: {self.name} | Price: {self.price} | Stock: {self.stock_quantity}"

    def update_price(self, new_price):
        self.price = new_price

    def reduce_stock(self, quantity):
        self.stock_quantity -= quantity

    def restock(self, quantity):
        self.stock_quantity += quantity

    def to_csv_row(self):
        return [self.product_id, self.name, self.price, self.stock_quantity]
