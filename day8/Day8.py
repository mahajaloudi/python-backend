
import math


class Shape:
    def __init__(self, name):
        self._name = name  

    def area(self):
        raise NotImplementedError("Subclass must implement area method")

    def perimeter(self):
        raise NotImplementedError("Subclass must implement perimeter method")

    def __str__(self):
        return f"This is a {self._name}"

    def __repr__(self):
        return f"Shape(name={self._name})"



class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.__radius = radius  

    def area(self):
        return math.pi * self.__radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.__radius

    def __str__(self):
        return f"{super().__str__()} with radius {self.__radius}"

    def get_radius(self):
        return self.__radius

    def set_radius(self, new_radius):
        if new_radius > 0:
            self.__radius = new_radius



class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

    def __str__(self):
        return f"{super().__str__()} with width {self.__width} and height {self.__height}"

    def __add__(self, other):  
        if isinstance(other, Rectangle):
            
            return Rectangle(self.__width + other.__width, self.__height + other.__height)
        return NotImplemented



def print_shape_info(shape_obj):
    print(shape_obj)
    print("Area:", shape_obj.area())
    print("Perimeter:", shape_obj.perimeter())
    print()



circle = Circle(radius=5)
rectangle1 = Rectangle(width=4, height=6)
rectangle2 = Rectangle(width=2, height=3)

print_shape_info(circle)
print_shape_info(rectangle1)

combined_rect = rectangle1 + rectangle2
print_shape_info(combined_rect)


circle.set_radius(10)
print("Updated Circle:", circle)
print("New Area:", circle.area())
