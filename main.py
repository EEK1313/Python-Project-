from customer import Customer
from product import Product
from order import Order
from payment import Payment
from file_handler import append_row

customers = []
products = []
orders = []
payments = []

def show_menu():
    print("\n--- E-Commerce Management System ---")
    print("1. Add customer")
    print("2. View customers")
    print("3. Add product")
    print("4. View products")
    print("5. Create order")
    print("6. View orders")
    print("7. Process payment")
    print("8. View payments")
    print("9. Exit")

def add_customer():
    customer_id = len(customers) + 1
    name = input("Enter customer name: ")
    email = input("Enter customer email: ")
    city = input("Enter customer city: ")

    customer = Customer(customer_id, name, email, city)
    customers.append(customer)
    append_row("data/customers.csv", customer.to_csv_row(), ["customer_id", "name", "email", "city"])
    print("Customer added successfully.")

def view_customers():
    for customer in customers:
        print(customer.display_info())

def add_product():
    try:
        product_id = len(products) + 1
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        stock_quantity = int(input("Enter stock quantity: "))

        product = Product(product_id, name, price, stock_quantity)
        products.append(product)
        append_row("data/products.csv", product.to_csv_row(), ["product_id", "name", "price", "stock_quantity"])
        print("Product added successfully.")
    except ValueError:
        print("Invalid input.")

def view_products():
    for product in products:
        print(product.display_info())

def find_product_by_id(product_id):
    for product in products:
        if product.product_id == product_id:
            return product
    return None

def create_order():
    try:
        customer_id = int(input("Enter customer ID: "))
        product_id = int(input("Enter product ID: "))
        quantity = int(input("Enter quantity: "))

        product = find_product_by_id(product_id)
        if product is None:
            print("Product not found.")
            return

        product.reduce_stock(quantity)

        order_id = len(orders) + 1
        order = Order(order_id, customer_id, product_id, quantity, product.price)
        orders.append(order)
        append_row("data/orders.csv", order.to_csv_row(), ["order_id", "customer_id", "product_id", "quantity", "unit_price", "total"])
        print("Order created successfully.")
        print(order.display_order())
    except ValueError:
        print("Invalid input.")

def view_orders():
    for order in orders:
        print(order.display_order())

def process_payment():
    try:
        order_id = int(input("Enter order ID: "))
        payment_method = input("Enter payment method: ")

        selected_order = None
        for order in orders:
            if order.order_id == order_id:
                selected_order = order
                break

        if selected_order is None:
            print("Order not found.")
            return

        payment_id = len(payments) + 1
        payment = Payment(payment_id, selected_order.order_id, selected_order.calculate_total(), payment_method)
        payment.process_payment()
        payments.append(payment)
        append_row("data/payments.csv", payment.to_csv_row(), ["payment_id", "order_id", "amount", "payment_method", "payment_status"])
        print("Payment processed successfully.")
        print(payment.display_payment())
    except ValueError:
        print("Invalid input.")

def view_payments():
    for payment in payments:
        print(payment.display_payment())

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_customer()
        elif choice == "2":
            view_customers()
        elif choice == "3":
            add_product()
        elif choice == "4":
            view_products()
        elif choice == "5":
            create_order()
        elif choice == "6":
            view_orders()
        elif choice == "7":
            process_payment()
        elif choice == "8":
            view_payments()
        elif choice == "9":
            print("Exiting program...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
