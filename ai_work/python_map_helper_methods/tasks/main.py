from map_operations import *

numbers = [1, 2, 3, 4, 5]

doubled = double_numbers(numbers)
squared = square_numbers(numbers)
even_numbers = filter_even_numbers(numbers)
total_sum = calculate_sum(numbers)

print("Numbers:", numbers)
print("Doubled numbers:", doubled)
print("Squared numbers:", squared)
print("Even numbers:", even_numbers)
print("Total sum of numbers:", total_sum)