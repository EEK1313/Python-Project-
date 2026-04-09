class Payment:
    def __init__(self, payment_id, order_id, amount, payment_method, payment_status="Pending"):
        self.payment_id = payment_id
        self.order_id = order_id
        self.amount = amount
        self.payment_method = payment_method
        self.payment_status = payment_status

    def process_payment(self):
        self.payment_status = "Completed"

    def refund_payment(self):
        self.payment_status = "Refunded"

    def update_method(self, new_method):
        self.payment_method = new_method

    def display_payment(self):
        return f"Payment ID: {self.payment_id} | Order ID: {self.order_id} | Amount: {self.amount} | Method: {self.payment_method} | Status: {self.payment_status}"

    def to_csv_row(self):
        return [self.payment_id, self.order_id, self.amount, self.payment_method, self.payment_status]
