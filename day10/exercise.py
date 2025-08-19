

# Exercise 1
class FibonacciIterator:
    def __init__(self, n):
        self.n = n       
        self.a, self.b = 0, 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        value = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return value

print("Exercise 1: Fibonacci Iterator (first 10 terms):")
for num in FibonacciIterator(10):
    print(num, end=" ")
print("\n" + "-"*50)



# Exercise 2
def alternating_signs(numbers):
    sign = 1
    for num in numbers:
        yield sign * num
        sign *= -1   

print("Exercise 2: Alternating Signs [1,2,3,4,5]:")
for val in alternating_signs([1, 2, 3, 4, 5]):
    print(val, end=" ")
print("\n" + "-"*50)



# Exercise 3
words = ["cat", "dog", "hi"]

ascii_dict = {
    word: {ch: ord(ch) for ch in word} for word in words
}

print("Exercise 3: Dictionary with ASCII mapping:")
print(ascii_dict)
print("-"*50)



# Exercise 4
text = "Hello World, Python is awesome!"

vowels = {ch.upper() for ch in text if ch.lower() in "aeiou"}

print("Exercise 4: Vowels in string (uppercase):")
print(vowels)
print("-"*50)



# Exercise 5
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

print("Exercise 5: First 6 primes:")
prime_gen = primes()
for _ in range(6):
    print(next(prime_gen), end=" ")
print("\n" + "-"*50)
