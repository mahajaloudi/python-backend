class MenuItem:
    """
    Represents a menu item with name, price, and category.
    """
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def display(self):
        """
        Return a formatted string describing the menu item.
        """
        return f"{self.name} ({self.category}) - ${self.price:.2f}"


class Order:
    """
    Represents a customer's order containing menu items.
    """
    def __init__(self):
        self.items = []

    def add_item(self, item):
        """
        Add a MenuItem to the order.
        """
        self.items.append(item)
        print(f"Added '{item.name}' to the order.")

    def remove_item(self, name):
        """
        Remove the first MenuItem with the given name from the order.
        """
        for item in self.items:
            if item.name.lower() == name.lower():
                self.items.remove(item)
                print(f"Removed '{item.name}' from the order.")
                return
        print(f"No item named '{name}' found in the order.")

    def calculate_total(self):
        """
        Calculate and return the total price of all items.
        """
        return sum(item.price for item in self.items)

    def display_order(self):
        """
        Display all items and the total price.
        """
        if not self.items:
            print("Order is empty.")
            return

        print("Order details:")
        for item in self.items:
            print(f" - {item.display()}")

        total = self.calculate_total()
        print(f"Total: ${total:.2f}")


# Example usage
if __name__ == "__main__":
    # Create some menu items
    item1 = MenuItem("Caesar Salad", 7.99, "Appetizer")
    item2 = MenuItem("Grilled Salmon", 15.99, "Main Course")
    item3 = MenuItem("Cheesecake", 6.50, "Dessert")

    # Create an order
    order = Order()

    # Add items
    order.add_item(item1)
    order.add_item(item2)
    order.add_item(item3)

    # Display order
    order.display_order()

    # Remove an item
    order.remove_item("Grilled Salmon")

    # Display updated order
    order.display_order()
