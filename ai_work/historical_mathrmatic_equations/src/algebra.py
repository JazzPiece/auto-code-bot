def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# Example usage
print(factorial(5))  # 120

def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Example usage
print(fibonacci(6))  # 5

import math

def quadratic_formula(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2*a)
        return x
    else:
        return "No real roots"

# Example usage
print(quadratic_formula(1, -3, 2))  # (2.0, 1.0)