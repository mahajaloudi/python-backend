
def call_counter(func):
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        print(f"Function '{func.__name__}' has been called {wrapper.call_count} times")
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper

@call_counter
def say_hello(name):
    return f"Hello, {name}!"

print(say_hello("Maha"))
print(say_hello("Ali"))
print(say_hello("Sara"))
