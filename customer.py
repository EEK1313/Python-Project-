class Customer:

    def __init__(self, customer_id, name, email, city):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.city = city

    def display_info(self):
        return f"ID: {self.customer_id} | Name: {self.name} | Email: {self.email} | City: {self.city}"

    def update_email(self, new_email):
        self.email = new_email

    def update_city(self, new_city):
        self.city = new_city

    def to_csv_row(self):
        return [self.customer_id, self.name, self.email, self.city]
