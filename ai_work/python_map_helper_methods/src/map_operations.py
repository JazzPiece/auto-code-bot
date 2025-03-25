def double_numbers(numbers):
    return list(map(lambda x: x * 2, numbers))

def square_numbers(numbers):
    return list(map(lambda x: x ** 2, numbers))

def filter_even_numbers(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))

def calculate_sum(numbers):
    return sum(numbers)