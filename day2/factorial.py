
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


if __name__== "__main__":
    number = int(input("Enter a number: "))
    print(f"The factorial of {number} is {factorial(number)}")