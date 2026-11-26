#Area and circumference of shapes
#Add a square. For a circle, also print the circumference. Show all results to 2 decimals.
import math
def area(shape , a , b=0):
    if shape == "circle":
        return math.pi*a*a
    elif shape == "rectangle":
        return a*b
    elif shape == "square":
        return  a*a
    elif shape == "triangle":
        return 0.5 *a *b
    else:
        return
print ("1.circle")  
print ("2.rectangle")
print ("3.triangle")
print("4.square")
choice = int(input("Enter shape:"))

if choice == 1:
    radius = float(input("Enter the radius of the circle: "))
    print("Area of the circle is:",area("circle", radius))
elif choice == 2:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    print("Area of the rectangle is:", area("rectangle", length, width))
elif choice == 3:
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    print("Area of the triangle is:",area("triangle", base, height))
elif choice == 4:
    side = float(input("Enter side of square:"))
    print("Area of circle",area("square",side) )    
else:
    print("Invalid choice. Please select a valid option.")
