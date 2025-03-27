def filter_even_numbers(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))

def filter_odd_numbers(numbers):
    return list(filter(lambda x: x % 2 != 0, numbers))