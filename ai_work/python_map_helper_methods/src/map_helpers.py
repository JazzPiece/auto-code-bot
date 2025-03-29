def filter_numbers(numbers, condition):
    return list(filter(condition, numbers))

def map_numbers(numbers, operation):
    return list(map(operation, numbers))

def calculate_sum(numbers):
    return sum(numbers)

def remove_duplicates(numbers):
    return list(set(numbers))

def triple_numbers(numbers):
    return list(map(lambda x: x * 3, numbers))