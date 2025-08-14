
class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.__price = price
        self.quantity = quantity

    def apply_discount(self, percent):
        discount = (percent / 100) * self.__price
        self.__price -= discount

    def restock(self, amount):
        if amount > 0:
            self.quantity += amount

    def get_price(self):
        return self.__price

    def __add__(self, other):
        if isinstance(other, Product) and self.product_id == other.product_id:
            return Product(self.product_id, self.name, self.__price, self.quantity + other.quantity)
        else:
            raise ValueError("Can't add different products")

    def __call__(self):
        return f"{self.name} (${self.__price:.2f}) - {self.quantity} in stock"


class DigitalProduct(Product):
    def __init__(self, product_id, name, price, quantity, file_size):
        super().__init__(product_id, name, price, quantity)
        self.file_size = file_size

    def apply_discount(self, percent):
        if percent > 20:
            percent = 20
        super().apply_discount(percent)


class PhysicalProduct(Product):
    def __init__(self, product_id, name, price, quantity, weight):
        super().__init__(product_id, name, price, quantity)
        self.weight = weight

    def apply_discount(self, percent):
        super().apply_discount(percent)
        if self.get_price() < 5:
            self._Product__price = 5  



print("🔹 Exercise 2: Product System")
p1 = DigitalProduct("D101", "Ebook", 50, 10, "500MB")
p2 = PhysicalProduct("P202", "Notebook", 8, 20, "0.5kg")
p3 = PhysicalProduct("P202", "Notebook", 8, 5, "0.5kg")

p1.apply_discount(30)  
p2.apply_discount(50)  
print(p1())
print(p2())

combined = p2 + p3
print(combined())
print()
