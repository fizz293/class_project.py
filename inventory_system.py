# Inventory Management System Code

# Import necessary libraries
import sys

# --- User Authentication and Role Management ---

class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role  # "Admin" or "User"

class AuthenticationService:
    def __init__(self):
        # Simple user storage with sample admin and user
        self.users = {
            "admin": User("admin", "admin123", "Admin"),
            "user": User("user", "user123", "User")
        }

    def login(self, username, password):
        user = self.users.get(username)
        if user and user.password == password:
            return user
        print("Invalid login credentials")
        return None

# --- Product Management ---

class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.product_id in self.products:
            print("Product ID already exists.")
        else:
            self.products[product.product_id] = product
            print("Product added successfully.")

    def edit_product(self, product_id, name=None, category=None, price=None, stock_quantity=None):
        product = self.products.get(product_id)
        if not product:
            print("Product not found.")
            return

        product.name = name if name else product.name
        product.category = category if category else product.category
        product.price = price if price else product.price
        product.stock_quantity = stock_quantity if stock_quantity else product.stock_quantity
        print("Product updated successfully.")

    def delete_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
            print("Product deleted successfully.")
        else:
            print("Product not found.")

    def view_all_products(self):
        if not self.products:
            print("No products in inventory.")
            return
        for product in self.products.values():
            print(f"{product.product_id} - {product.name}, Category: {product.category}, "
                  f"Price: {product.price}, Stock: {product.stock_quantity}")

    def search_product(self, name=None, category=None):
        for product in self.products.values():
            if (name and product.name == name) or (category and product.category == category):
                print(f"Found: {product.product_id} - {product.name}, Category: {product.category}, "
                      f"Price: {product.price}, Stock: {product.stock_quantity}")

    def adjust_stock(self, product_id, amount):
        product = self.products.get(product_id)
        if not product:
            print("Product not found.")
            return
        product.stock_quantity += amount
        print(f"Stock updated. New stock quantity: {product.stock_quantity}")

    def check_stock_levels(self, threshold=5):
        for product in self.products.values():
            if product.stock_quantity <= threshold:
                print(f"Low stock alert for {product.name}: {product.stock_quantity} left.")

# --- Console-based Application ---

def main():
    auth_service = AuthenticationService()
    inventory = Inventory()

    # User Login
    print("Welcome to the Inventory Management System")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    user = auth_service.login(username, password)
    if not user:
        sys.exit()

    # Main Menu
    while True:
        if user.role == "Admin":
            print("\n1. Add Product\n2. Edit Product\n3. Delete Product\n4. View All Products\n"
                  "5. Search Product\n6. Adjust Stock\n7. Check Stock Levels\n8. Logout")
        else:
            print("\n1. View All Products\n2. Search Product\n3. Logout")

        choice = int(input("Enter your choice: "))

        if user.role == "Admin":
            if choice == 1:
                product_id = input("Enter product ID: ")
                name = input("Enter product name: ")
                category = input("Enter category: ")
                price = float(input("Enter price: "))
                stock_quantity = int(input("Enter stock quantity: "))
                product = Product(product_id, name, category, price, stock_quantity)
                inventory.add_product(product)
            elif choice == 2:
                product_id = input("Enter product ID to edit: ")
                name = input("Enter new name (leave blank to keep current): ")
                category = input("Enter new category (leave blank to keep current): ")
                price = input("Enter new price (leave blank to keep current): ")
                stock_quantity = input("Enter new stock quantity (leave blank to keep current): ")
                price = float(price) if price else None
                stock_quantity = int(stock_quantity) if stock_quantity else None
                inventory.edit_product(product_id, name, category, price, stock_quantity)
            elif choice == 3:
                product_id = input("Enter product ID to delete: ")
                inventory.delete_product(product_id)
            elif choice == 4:
                inventory.view_all_products()
            elif choice == 5:
                name = input("Enter product name to search (leave blank if not searching by name): ")
                category = input("Enter category to search (leave blank if not searching by category): ")
                inventory.search_product(name, category)
            elif choice == 6:
                product_id = input("Enter product ID to adjust stock: ")
                amount = int(input("Enter amount to adjust (positive to restock, negative to reduce): "))
                inventory.adjust_stock(product_id, amount)
            elif choice == 7:
                threshold = int(input("Enter stock threshold to check for low stock: "))
                inventory.check_stock_levels(threshold)
            elif choice == 8:
                print("Logging out.")
                break
        else:
            if choice == 1:
                inventory.view_all_products()
            elif choice == 2:
                name = input("Enter product name to search: ")
                category = input("Enter category to search: ")
                inventory.search_product(name, category)
            elif choice == 3:
                print("Logging out.")
                break

if __name__ == "__main__":
    main()
