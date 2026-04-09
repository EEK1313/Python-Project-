class Order:
    def __init__(self, order_id, customer_id, product_id, quantity, unit_price):
        self.order_id = order_id
        self.customer_id = customer_id
        self.product_id = product_id
        self.quantity = quantity
        self.unit_price = unit_price

    def calculate_total(self):
        return self.quantity * self.unit_price

    def display_order(self):
        return f"Order ID: {self.order_id} | Customer ID: {self.customer_id} | Product ID: {self.product_id} | Quantity: {self.quantity} | Total: {self.calculate_total()}"

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity

    def to_csv_row(self):
        return [self.order_id, self.customer_id, self.product_id, self.quantity, self.unit_price, self.calculate_total()]
