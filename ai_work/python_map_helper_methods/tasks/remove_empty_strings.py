def remove_empty_strings(strings):
    return list(filter(lambda x: x != '', strings))

filename: filter_divisible_by.py
code:
def filter_divisible_by(numbers, divisor):
    return list(filter(lambda x: x % divisor == 0, numbers))