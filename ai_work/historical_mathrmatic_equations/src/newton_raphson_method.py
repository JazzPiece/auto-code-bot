import math

def newton_raphson_method(f, f_prime, initial_guess, tolerance=1e-6):
    x = initial_guess
    while abs(f(x)) > tolerance:
        x = x - f(x) / f_prime(x)
    return x

# Example usage
f = lambda x: x**2 - 4
f_prime = lambda x: 2*x
print(newton_raphson_method(f, f_prime, 3))  # 2.0