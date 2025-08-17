

def multiplier(base):
    def inner(x):
        if base == 0:  
            return x * x
        return base * x
    return inner


doubler = multiplier(2)
tripler = multiplier(3)
squarer = multiplier(0)

print("Doubler(5):", doubler(5))   
print("Tripler(5):", tripler(5))   
print("Squarer(5):", squarer(5))   
