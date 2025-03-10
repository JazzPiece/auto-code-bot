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

def surface_area_of_cylinder(radius, height):
    return 2 * math.pi * radius * (radius + height)

# Example usage
print(surface_area_of_cylinder(2, 5))  # 94.2

def volume_of_cone(radius, height):
    return (1/3) * math.pi * radius**2 * height

# Example usage
print(volume_of_cone(3, 4))  # 37.7