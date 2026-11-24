#Area of Different Shapes Using Function Polymorphism
import math
def calculate_area (shape, a ,b=0):
    if shape == "rectangle":
        return a*b
    elif shape == "circle":
        return math.pi *a*a
    elif shape == "triangle":
        return 0.5*a*b

print ("1.circle")  
print ("2.rectangle")
print ("3.triangle")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    radius = float(input("Enter the radius of the circle: "))
    print("Area of the circle is:", calculate_area("circle", radius))
elif choice == 2:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    print("Area of the rectangle is:", calculate_area("rectangle", length, width))
elif choice == 3:
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    print("Area of the triangle is:", calculate_area("triangle", base, height))
else:
    print("Invalid choice. Please select a valid option.")
