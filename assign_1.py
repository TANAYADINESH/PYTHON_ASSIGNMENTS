# basic calculator 
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Check if first number is even or odd")
print("6. Exponentiation")
choice=int(input("Enter choice(1/2/3/4/5/6): "))
if choice==1:
    print(a,"+",b,"=",a+b)
elif choice==2:
    print(a,"-",b,"=",a-b)
elif choice==3:
    print(a,"*",b,"=",a*b)     
elif choice==4:
    print(a,"/",b,"=",a/b)
elif choice==5:
    if(a%2==0):
        print(a,"is even")
    else:
        print(a,"is odd")
elif choice==6:
    print(f'The power of {a} to {b} is {a**b}')
else:
    print("Invalid choice")


