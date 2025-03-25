def count_even_odd(arr):
    even_count = len([num for num in arr if num % 2 == 0])
    odd_count = len(arr) - even_count
    return even_count, odd_count