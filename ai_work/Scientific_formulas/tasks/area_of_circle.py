import math

def calculate_area(radius):
    return math.pi * radius**2

radius = float(input("Enter the radius of the circle: "))
area = calculate_area(radius)
print(f"The area of the circle with radius {radius} is {area}")