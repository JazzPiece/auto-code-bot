def map_operations(numbers, operation):
    return list(map(operation, numbers))

def calculate_sum(numbers):
    return sum(numbers)

def remove_duplicates(numbers):
    return list(set(numbers))

def triple_numbers(numbers):
    return list(map(lambda x: x * 3, numbers))

def double_numbers(numbers):
    return list(map(lambda x: x * 2, numbers))

def square_numbers(numbers):
    return list(map(lambda x: x ** 2, numbers))