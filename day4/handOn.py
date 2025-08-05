def manipulate_data(numbers: list) -> dict:
    # Sort the list
    sorted_numbers = sorted(numbers)

    # Filter out even numbers
    filtered_numbers = [num for num in numbers if num % 2 != 0]

    # Transform: Square each number
    squared_numbers = [num ** 2 for num in numbers]

    return {
        "sorted": sorted_numbers,
        "filtered": filtered_numbers,
        "transformed": squared_numbers
    }


def manipulate_tuples(data: tuple) -> dict:
    sorted_tuple = tuple(sorted(data))
    filtered_tuple = tuple(num for num in data if num % 2 != 0)
    squared_tuple = tuple(num ** 2 for num in data)

    return {
        "sorted": sorted_tuple,
        "filtered": filtered_tuple,
        "transformed": squared_tuple
    }


if __name__ == "__main__":
    numbers_list = [10, 3, 5, 8, 1, 4]
    numbers_tuple = (7, 2, 9, 5, 6)

    print("List manipulation results:")
    print(manipulate_data(numbers_list))

    print("\nTuple manipulation results:")
    print(manipulate_tuples(numbers_tuple))
