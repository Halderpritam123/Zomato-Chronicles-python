# Create an empty menu
menu = []

# Initialize order ID counter as a global variable
order_id_counter = 1

# Initialize orders list
orders = []

# User authentication data
users = [{'username': 'user1', 'password': 'pass1'}, {'username': 'user2', 'password': 'pass2'}]
current_user = None

# Signup function
def signup():
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    # Check if the username is already taken
    for user in users:
        if user['username'] == username:
            print("Username already exists. Please try again.")
            return

    # Add the new user to the user list
    users.append({'username': username, 'password': password})
    print("Signup successful!")

# Login function
def login():
    global current_user
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the username and password match
    for user in users:
        if user['username'] == username and user['password'] == password:
            current_user = user
            print(f"Welcome, {username}!")
            return

    print("Invalid username or password.")

# Logout function
def logout():
    global current_user
    current_user = None
    print("Logged out successfully.")

# Function to print the menu in tabular format
def print_menu():
    if len(menu) == 0:
        print("Menu is empty.")
    else:
        print("Menu:")
        print("-------------------------------------------------------")
        print("| Dish ID |   Dish Name   |   Price   |   Availability  |")
        print("-------------------------------------------------------")
        for dish in menu:
            print(f"| {dish['dish_id']:7} | {dish['dish_name']:<13} | {dish['price']:9.2f} | {dish['availability']:<14} |")
        print("-------------------------------------------------------")

# Function to add a new dish to the menu
def add_dish():
    if current_user:
        dish_id = input("Enter the dish ID: ")
        dish_name = input("Enter the dish name: ")
        price = float(input("Enter the price: "))
        availability = input("Is the dish available (yes/no): ")

        dish = {
            'dish_id': dish_id,
            'dish_name': dish_name,
            'price': price,
            'availability': availability
        }

        menu.append(dish)
        print("Dish added to the menu successfully!")
        print_menu()  # Print the updated menu
    else:
        print("Please login to access this feature.")

# Function to remove a dish from the menu
def remove_dish():
    if current_user:
        dish_id = input("Enter the dish ID to remove: ")

        for dish in menu:
            if dish['dish_id'] == dish_id:
                menu.remove(dish)
                print("Dish removed from the menu successfully!")
                print_menu()  # Print the updated menu
                return

        print("Dish ID not found in the menu.")
    else:
        print("Please login to access this feature.")

# Function to update the availability of a dish
def update_availability():
    if current_user:
        dish_id = input("Enter the dish ID to update availability: ")

        for dish in menu:
            if dish['dish_id'] == dish_id:
                availability = input("Is the dish available (yes/no): ")
                dish['availability'] = availability
                print("Availability updated successfully!")
                print_menu()  # Print the updated menu
                return

        print("Dish ID not found in the menu.")
    else:
        print("Please login to access this feature.")

# Function to take a new order from a customer
def take_order():
    global order_id_counter  # Declare order_id_counter as a global variable

    if current_user:
        customer_name = input("Enter customer name: ")
        dish_ids = input("Enter dish IDs (comma-separated): ").split(',')

        # Check if the ordered dishes are available
        available_dishes = []
        unavailable_dishes = []

        for dish_id in dish_ids:
            for dish in menu:
                if dish['dish_id'] == dish_id:
                    if dish['availability'].lower() == 'yes':
                        available_dishes.append(dish)
                    else:
                        unavailable_dishes.append(dish)
                    break

        if len(unavailable_dishes) > 0:
            print("The following dishes are not available:")
            for dish in unavailable_dishes:
                print(f"- {dish['dish_name']}")
            print("Please choose from the available dishes.")
            return

        # Process the order
        order = {
            'order_id': order_id_counter,
            'customer_name': customer_name,
            'dishes': available_dishes,
            'status': 'received'
        }

        orders.append(order)
        order_id_counter += 1
        print("Order placed successfully!")
    else:
        print("Please login to access this feature.")

# Function to update the status of an order
def update_order_status():
    if current_user:
        order_id = int(input("Enter the order ID to update status: "))

        for order in orders:
            if order['order_id'] == order_id:
                status = input("Enter the new status: ")
                order['status'] = status
                print("Order status updated successfully!")
                return

        print("Order ID not found.")
    else:
        print("Please login to access this feature.")


# show all orders 
def show_all_orders():
        if len(orders) == 0:
            print("No orders to review.")
        else:
            print("Orders:")
            print("---------------------------------------------------")
            print("| Order ID |   Customer Name   |   Price   | Status |")
            print("---------------------------------------------------")
            for order in orders:
                order_id = order['order_id']
                customer_name = order['customer_name']
                total_price = calculate_order_price(order)
                status = order['status']
                print(f"| {order_id:8} | {customer_name:<17} | ${total_price:<8.2f} | {status:<6} |")
            print("---------------------------------------------------")
# Function to review all orders

def review_orders():
    if current_user:
        if len(orders) == 0:
            print("No orders to review.")
        else:
            print("Orders:")
            print("---------------------------------------------------")
            print("| Order ID |   Customer Name   |   Price   | Status |")
            print("---------------------------------------------------")
            for order in orders:
                order_id = order['order_id']
                customer_name = order['customer_name']
                total_price = calculate_order_price(order)
                status = order['status']
                print(f"| {order_id:8} | {customer_name:<17} | ${total_price:<8.2f} | {status:<6} |")
            print("---------------------------------------------------")
    else:
        print("Please login to access this feature.")

# Function to calculate the total price of an order
def calculate_order_price(order):
    total_price = 0
    for dish in order['dishes']:
        total_price += dish['price']
    return total_price

# Function to filter orders based on status
def filter_orders_by_status(status):
    filtered_orders = [order for order in orders if order['status'] == status]
    if len(filtered_orders) == 0:
        print(f"No orders with status '{status}'.")
    else:
        print(f"Orders with status '{status}':")
        for order in filtered_orders:
            print(f"Order ID: {order['order_id']}")
            print(f"Customer Name: {order['customer_name']}")
            print(f"Total Price: ${calculate_order_price(order):.2f}")
            print()

# Function to save the menu and orders to a file
def save_data_to_file():
    with open('menu.txt', 'w') as menu_file:
        for dish in menu:
            menu_file.write(f"{dish['dish_id']},{dish['dish_name']},{dish['price']},{dish['availability']}\n")

    with open('orders.txt', 'w') as orders_file:
        for order in orders:
            orders_file.write(f"{order['order_id']},{order['customer_name']},{order['status']}\n")
            for dish in order['dishes']:
                orders_file.write(f"{dish['dish_id']}\n")

# Function to load the menu and orders from a file
def load_data_from_file():
    global order_id_counter

    try:
        with open('menu.txt', 'r') as menu_file:
            for line in menu_file:
                dish_id, dish_name, price, availability = line.strip().split(',')
                dish = {
                    'dish_id': dish_id,
                    'dish_name': dish_name,
                    'price': float(price),
                    'availability': availability
                }
                menu.append(dish)

        with open('orders.txt', 'r') as orders_file:
            for line in orders_file:
                order_id, customer_name, status = line.strip().split(',')
                order = {
                    'order_id': int(order_id),
                    'customer_name': customer_name,
                    'dishes': [],
                    'status': status
                }
                orders.append(order)
                order_id_counter = max(order_id_counter, int(order_id) + 1)
    except FileNotFoundError:
        print("Data files not found. Starting with empty menu and orders.")

# Function to exit the program
def exit_program():
    print("Exiting the program. Have a nice day!")
    save_data_to_file()  # Save menu and orders to files
    exit()

# Main program loop
def main():
    load_data_from_file()

    while True:
        print("Welcome to Zesty Zomato")
        print("1. Signup")
        print("2. Login")
        print("3. Logout")
        print("4. Add Dish to Menu")
        print("5. Remove Dish from Menu")
        print("6. Update Dish Availability")
        print("7. Take Order")
        print("8. Update Order Status")
        print("9. Review Orders")
        print("10. Filter Orders by Status")
        print("11. Show All Orders")
        print("12. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            signup()
        elif choice == '2':
            login()
        elif choice == '3':
            logout()
        elif choice == '4':
            add_dish()
        elif choice == '5':
            remove_dish()
        elif choice == '6':
            update_availability()
        elif choice == '7':
            take_order()
        elif choice == '8':
            update_order_status()
        elif choice == '9':
            review_orders()
        elif choice == '10':
            status = input("Enter the status to filter orders: ")
            filter_orders_by_status(status)
        elif choice == '11':
            show_all_orders()
        elif choice == '12':
            exit_program()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
