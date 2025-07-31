
def fibonacci_series(n):
    if n <= 0:
        raise ValueError("Number of terms must be greater than 0.")

    series = [0, 1] if n > 1 else [0]

    for i in range(2, n):
        next_term = series[-1] + series[-2]
        series.append(next_term)

    return series


if __name__== "__main__":
    terms = int(input("Enter the number of terms: "))
    print(f"Fibonacci series with {terms} terms: {fibonacci_series(terms)}")
