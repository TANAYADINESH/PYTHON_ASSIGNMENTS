# weight calculator on earth and moon using functions
def weight_on_earth(weight):
    return weight * 9.81

def weight_on_moon(weight):
    return weight * 1.62

weight = float(input("Enter your weight in kilograms: "))

print("\nSelect Planet:")
print("1. Earth") 
print("2. Moon")

choice = int(input("\nEnter your choice (1-2): "))

if choice == 1:
    result = weight_on_earth(weight)
    print(f"\nYour weight on Earth is: {result:.2f} N")

elif choice == 2:
    result = weight_on_moon(weight)
    print(f"\nYour weight on the Moon is: {result:.2f} N")

else:
    print("\nInvalid choice! Please select between 1 and 2.")
