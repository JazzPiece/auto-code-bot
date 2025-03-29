def remove_duplicates(numbers):
    return list(set(numbers))

def remove_unique_numbers(numbers):
    return list(filter(lambda x: numbers.count(x) == 1, numbers))

def keep_duplicates(numbers):
    return list(filter(lambda x: numbers.count(x) > 1, numbers))