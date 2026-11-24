
# Python Calculator Program

try:    
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("\nSelect Operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exponentiation (**)")
    print("6. Modulus (%)")

    choice = int(input("\nEnter your choice (1-6): "))


    if choice == 1:
        result = a + b
        print("\nResult of Addition =", result)

    elif choice == 2:
        result = a - b
        print("\nResult of Subtraction =", result)

    elif choice == 3:
        result = a * b
        print("\nResult of Multiplication =", result)

    elif choice == 4:
        if b == 0:
            print("\nError: Division by zero is not allowed.")
        else:
            result = a / b
            print("\nResult of Division =", result)

    elif choice == 5:
        result = a ** b
        print("\nResult of Exponentiation =", result)

    elif choice == 6:
        if b == 0:
            print("\nError: Modulus by zero is not allowed.")
        else:
            result = a % b
            print("\nResult of Modulus =", result)

    else:
        print("\nInvalid choice! Please select between 1 and 6.")

except ValueError:
    print("\nInvalid Input! Please enter valid numbers and a valid choice.")

except OverflowError:
    print("\nError: Result is too large to calculate.")

