def separate_even_odd(arr):
    even = [num for num in arr if num % 2 == 0]
    odd = [num for num in arr if num % 2 != 0]
    return even, odd