


def add(a: int, b: int) -> int:
    """Return the sum of two numbers."""
    return a + b

def divide(a: int, b: int) -> float:
    """Return the division of a by b. Raises ValueError if b=0."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def greet_user(name: str, prefix: str = "Hello") -> str:
    """Return a greeting message with default prefix."""
    return f"{prefix}, {name}!"

class Calculator:
    """Simple calculator class with multiply method."""
    
    def multiply(self, a: int, b: int) -> int:
        return a * b
