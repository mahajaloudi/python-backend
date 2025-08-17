
import time


def multiplier(base):
    """Closure that creates a custom multiplier.
       Special case: base=0 → square numbers."""
    def inner(x):
        if base == 0:
            return x * x
        return base * x
    return inner

doubler = multiplier(2)
tripler = multiplier(3)
squarer = multiplier(0)

print("=== Closure Example ===")
print("Doubler(5):", doubler(5))
print("Tripler(5):", tripler(5))
print("Squarer(5):", squarer(5))
print()


def call_counter(func):
    """Counts how many times a function has been called."""
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        print(f"Function '{func.__name__}' has been called {wrapper.call_count} times")
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper

@call_counter
def say_hello(name):
    return f"Hello, {name}!"

print("=== Call Counter Decorator ===")
print(say_hello("Maha"))
print(say_hello("Ali"))
print(say_hello("Sara"))
print()


def validate_positive(func):
    """Ensures that all numeric arguments are positive numbers."""
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg <= 0:
                raise ValueError(f"Invalid input {arg}: All numbers must be positive")
        return func(*args, **kwargs)
    return wrapper

@validate_positive
def add(a, b):
    return a + b

print("=== Input Validator Decorator ===")
print("Add(3, 4):", add(3, 4))
try:
    print("Add(-2, 5):", add(-2, 5))  
except ValueError as e:
    print("Error:", e)
print()


def execution_timer(func):
    """Measures how long a function takes to run."""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function '{func.__name__}' executed in {end - start:.6f} seconds")
        return result
    return wrapper

@execution_timer
def slow_function(n):
    """Simulates a slow function by sleeping."""
    time.sleep(n)
    return f"Finished after {n} seconds"

print("=== Execution Timer Decorator ===")
print(slow_function(2))
