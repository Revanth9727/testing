def divide(a, b):
    # BUG: no check for b == 0 — raises ZeroDivisionError
    return a / b


def get_first(items):
    # BUG: crashes with IndexError on an empty list
    return items[0] if items else None


def get_user_name(user):
    # BUG: KeyError if "name" key is missing
    return user["name"]


def calculate_average(numbers):
    # BUG: divides by len which is 0 for an empty list
    total = sum(numbers)
    return total / len(numbers)


if __name__ == "__main__":
    print(divide(10, 2))
    print(get_first([1, 2, 3]))
    print(get_user_name({"name": "Alice"}))
    print(calculate_average([4, 5, 6]))
