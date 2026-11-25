#Palindrome check
#Take a string and check whether it is a palindrome, ignoring case and spaces.

a = input("Enter a string:").lower().replace(" " , "")
if a== a[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")    
