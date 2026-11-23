
import math

def calculate_area(shape, a, b=0):
    if shape == "circle":
        return math.pi * a * a
    elif shape == "rectangle":
        return a * b
    elif shape == "triangle":
        return 0.5 * a * b
    else:
        return "Invalid shape"


# Main Program
radius = float(input("Enter radius of circle: "))
print("Area of Circle =", calculate_area("circle", radius))

length = float(input("\nEnter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))
print("Area of Rectangle =", calculate_area("rectangle", length, breadth))

base = float(input("\nEnter base of triangle: "))
height = float(input("Enter height of triangle: "))
print("Area of Triangle =", calculate_area("triangle", base, height))
