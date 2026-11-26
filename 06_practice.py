#Password checker: strong, medium, weak (06)
#Check length of 8 or more, uppercase, lowercase, digit and special character. 5 checks passed = Strong, 3 or 4 = Medium, otherwise Weak.

while True:
    password = input("Enter the password or exit:")
    if password == 'exit':
     break
     
    checks = [
        len(password) >= 8,
        any(ch.isupper() for ch in password),
        any(ch.islower()for ch in password),
        any(ch.isdigit()for ch in password),
        any(not ch.isalnum()for ch in password),
    ]
    score = sum(checks)

    if score == 5:
       print("Strong password")
    elif score >= 1:
       print("Mediun password")
    else:
       print("Weak password")      