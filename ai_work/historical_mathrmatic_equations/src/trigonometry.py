import math

def area_of_triangle(base, height):
    return 0.5 * base * height

# Example usage
print(area_of_triangle(4, 6))  # 12.0

def distance_formula(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Example usage
print(distance_formula(1, 2, 4, 6))  # 5.0

def pythagorean_theorem(a, b):
    c = math.sqrt(a**2 + b**2)
    return c

# Example usage
print(pythagorean_theorem(3, 4))  # 5.0