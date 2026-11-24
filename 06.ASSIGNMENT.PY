# password strength checker

while True:
    password = input("Enter the password or type 'exit' to quit: ")
    if password == "exit":
        break

    if len(password) >=8 and any(ch.isupper()for ch in password)and any(ch.islower()for ch in password):
        print("Password is strong.")
    else:
        print("Password is weak. Please try again.")