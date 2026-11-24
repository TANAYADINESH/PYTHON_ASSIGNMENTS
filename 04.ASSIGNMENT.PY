#Secret Message Decoder 

substring = input("Enter the secret message: ")
string = input("Enter the substring to decode: ")

if substring in string:
    print("The substring is present in the secret message.")
else:
    print("The substring is not present in the secret message.")    