import statistics

def calculate_standard_deviation(numbers):
    return statistics.stdev(numbers)

result = calculate_standard_deviation([1, 2, 3, 4, 5])
print(result)