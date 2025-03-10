import math

def surface_area_of_cylinder(radius, height):
    return 2 * math.pi * radius * (radius + height)

# Example usage
print(surface_area_of_cylinder(2, 5))  # 94.2