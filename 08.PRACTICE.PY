#Swap first and last character
#Take a string and swap its first and last characters.

# Swap first and last character

a = input("Enter the string: ").lower()

if len(a) < 2:
    print(a)
else:
    print(a[-1] + a[1:-1] + a[0])
