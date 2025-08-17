

def validate_positive(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg <= 0:
                raise ValueError(f"Invalid input {arg}: All numbers must be positive")
        return func(*args, **kwargs)
    return wrapper

@validate_positive
def add(a, b):
    return a + b

print("Add(3, 4):", add(3, 4))   

