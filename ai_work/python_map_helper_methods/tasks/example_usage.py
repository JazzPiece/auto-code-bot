from enhanced_map_helpers import *

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = filter_numbers(numbers, lambda x: x % 2 == 0)
print(even_numbers)

doubled_numbers = map_numbers(numbers, lambda x: x * 2)
print(doubled_numbers)

total_sum = calculate_sum(numbers)
print(total_sum)

unique_numbers = remove_duplicates(numbers)
print(unique_numbers)