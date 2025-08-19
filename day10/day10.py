

class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        else:
            val = self.current
            self.current -= 1
            return val


print("Iterables & Iterators Example:")
for num in CountDown(5):
    print(num, end=" ")
print("\n" + "-" * 50)


def simple_generator():
    yield "First value"
    yield "Second value"
    yield "Third value"


print("Generator Example:")
for val in simple_generator():
    print(val)
print("-" * 50)



nums = [1, 2, 3, 4, 5]


squares = [n ** 2 for n in nums]


num_dict = {n: n ** 2 for n in nums}


num_set = {n % 2 for n in nums}

print("List comprehension (squares):", squares)
print("Dictionary comprehension:", num_dict)
print("Set comprehension:", num_set)
print("-" * 50)


def fibonacci_generator(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


print("Fibonacci Generator (limit 50):")
for val in fibonacci_generator(50):
    print(val, end=" ")
print("\n" + "-" * 50)



def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_generator():
    num = 2
    while True:  
        if is_prime(num):
            yield num
        num += 1


print("Prime Number Generator (first 10 primes):")
prime_gen = prime_generator()
for _ in range(10):
    print(next(prime_gen), end=" ")
print("\n" + "-" * 50)
