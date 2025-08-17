
import time
from functools import wraps


def power_function(exponent):
    """Closure that remembers the exponent value."""
    def inner(base):
        return base ** exponent
    return inner


square = power_function(2)
cube = power_function(3)


def execution_timer(func):
    """Decorator to measure execution time of a function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)   
        end = time.time()
        execution_time = end - start
        print(f"Function '{func.__name__}' executed in {execution_time:.6f} seconds")
        return result
    return wrapper


def uppercase_output(func):
    """Decorator that converts function output to uppercase (if string)."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result.upper()
        return result
    return wrapper


class FileWriter:
    """Custom context manager for file handling."""
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode, encoding="utf-8")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()



@execution_timer
def slow_function(n):
    """A slow function that simulates work by sleeping."""
    time.sleep(n)
    return f"Finished after {n} seconds"

@uppercase_output
def greet(name):
    return f"Hello, {name}!"

def main():
   
    print("Closure Examples:")
    print("Square of 5:", square(5))
    print("Cube of 3:", cube(3))
    print()

   
    print("Decorator Examples:")
    print(greet("maha"))   
    print(slow_function(2))  
    print()

    with FileWriter("results.txt", "w") as f:
        f.write("Closure Results:\n")
        f.write(f"Square(5) = {square(5)}\n")
        f.write(f"Cube(3) = {cube(3)}\n\n")

        f.write("Decorator Results:\n")
        f.write(f"Greet: {greet('maha')}\n")
        f.write(f"Slow Function Result: {slow_function(1)}\n")

    print("Results saved to results.txt")

if __name__ == "__main__":
    main()
