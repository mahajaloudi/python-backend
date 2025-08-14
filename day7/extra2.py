class Dog:
    """
    A class to represent a dog.
    """

    # Class variable (shared across all instances unless overridden)
    species = "Canis familiaris"

    def __init__(self, name, breed):
        """
        Initialize name and breed.
        """
        self.name = name
        self.breed = breed

    def describe(self):
        """
        Return a description string.
        """
        return f"{self.name} is a {self.breed}. Species: {self.species}."


# Create two Dog instances
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Beagle")

# Display initial descriptions
print(dog1.describe())
print(dog2.describe())

# Modify species for dog1 only (creates instance attribute, doesn't change class variable)
dog1.species = "Canis lupus"

# Display descriptions after modification
print("\nAfter modifying dog1's species:")
print(dog1.describe())  # Uses modified species for dog1
print(dog2.describe())  # Still uses the class variable
