def filter_even_numbers(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))

def filter_odd_numbers(numbers):
    return list(filter(lambda x: x % 2 != 0, numbers))

def filter_negative_numbers(numbers):
    return list(filter(lambda x: x < 0, numbers))

def filter_positive_numbers(numbers):
    return list(filter(lambda x: x > 0, numbers))

def double_numbers(numbers):
    return list(map(lambda x: x * 2, numbers))

def square_numbers(numbers):
    return list(map(lambda x: x ** 2, numbers))