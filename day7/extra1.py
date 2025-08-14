class Person:
    """
    A class to represent a person.
    """

    def __init__(self, name, age):
        """
        Initialize name and age.
        """
        self.name = name
        self.age = age

    def introduce(self):
        """
        Return an introduction string.
        """
        return f"Hello, my name is {self.name} and I am {self.age} years old."


# Create instances
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Call introduce() and print results
print(person1.introduce())
print(person2.introduce())
