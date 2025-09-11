
import sqlite3


conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    stock INTEGER NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
)
''')

conn.commit()



class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self._stock = stock  

    def __str__(self):
        return f"{self.name} - ${self.price} - Stock: {self._stock}"

    @property
    def stock(self):
        return self._stock

    def update_stock(self, quantity):
        if quantity > self._stock:
            raise ValueError("❌ Not enough stock!")
        self._stock -= quantity



class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cart = ShoppingCart()


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity):
        if quantity > product.stock:
            print(f"❌ Not enough stock for {product.name}")
            return
        self.items.append((product, quantity))
        print(f"✅ Added {quantity} x {product.name} to cart")

    def view_cart(self):
        if not self.items:
            print("\nYour cart is empty\n")
            return
        print("\n=== Shopping Cart ===")
        total = 0
        for idx, (p, qty) in enumerate(self.items, 1):
            subtotal = p.price * qty
            print(f"{idx}. {p.name} x {qty} = ${subtotal}")
            total += subtotal
        print(f"Total: ${total}")
        print("====================\n")

    def checkout(self):
        if not self.items:
            print("❌ Cart is empty, cannot checkout.")
            return
        total = 0
        for p, qty in self.items:
            try:
                p.update_stock(qty)
                cursor.execute(
                    "UPDATE products SET stock=? WHERE name=?",
                    (p.stock, p.name)
                )
                total += p.price * qty
            except ValueError as e:
                print(e)
        conn.commit()
        print(f"✅ Checkout complete! Total paid: ${total}")
        self.items.clear()



def add_product_to_db(name, price, stock):
    cursor.execute(
        "INSERT INTO products (name, price, stock) VALUES (?, ?, ?)",
        (name, price, stock)
    )
    conn.commit()


def get_all_products():
    cursor.execute("SELECT name, price, stock FROM products")
    products = cursor.fetchall()
    return [Product(name, price, stock) for name, price, stock in products]



def main():
    print("=== Simple E-commerce Store Backend ===\n")



    user_name = input("Enter your name: ")
    user_email = input("Enter your email: ")
    user = User(user_name, user_email)

    while True:
        print("\n1. View Products")
        print("2. Add Product to Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            products = get_all_products()
            print("\n=== Products ===")
            for idx, p in enumerate(products, 1):
                print(f"{idx}. {p}")
        elif choice == "2":
            products = get_all_products()
            for idx, p in enumerate(products, 1):
                print(f"{idx}. {p}")
            try:
                prod_idx = int(input("Select product number: ")) - 1
                qty = int(input("Enter quantity: "))
                user.cart.add_product(products[prod_idx], qty)
            except (ValueError, IndexError):
                print("❌ Invalid selection or quantity")
        elif choice == "3":
            user.cart.view_cart()
        elif choice == "4":
            user.cart.checkout()
        elif choice == "5":
            print("👋 Exiting store...")
            break
        else:
            print("❌ Invalid choice!")


if __name__ == "__main__":
    main()
