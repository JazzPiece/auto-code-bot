import math

def distance_formula(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Example usage
print(distance_formula(1, 2, 4, 6))  # 5.0