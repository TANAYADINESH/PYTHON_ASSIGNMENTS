#Calculator with floor division, loop and 2 decimals (01)
#Take two numbers and an operator (+ - * / // % **). Print the result up to 2 decimal places. Repeat until the user chooses to exit.

while True:
    a=float(input("Enter the first number: "))
    b=float(input("Enter the second number: "))
    operator=input("Enter the operator (+, -, *, /, //, %, **): ")

    if operator in("/", "//", "%", "**") and b==0:
        print("Error: Division by zero is not allowed.")
    elif operator=="+":
        print(f"Result: {a+b:.2f}")
    elif operator=="-":
        print(f"Result: {a-b:.2f}")
    elif operator=="*":
        print(f"Result: {a*b:.2f}")
    elif operator=="/":
        print(f"Result: {a/b:.2f}")
    elif operator=="//":
        print(f"Result: {a//b:.2f}")
    elif operator=="%":
        print(f"Result: {a%b:.2f}")
    elif operator=="**":
        print(f"Result: {a**b:.2f}")
    else:
        print("Invalid operator. Please try again.")

    choice=input("Do you want to perform another calculation? (yes/no): ")
    if choice.lower()!="yes":
        break
    if choice.lower()=="no":
        print("Exit")