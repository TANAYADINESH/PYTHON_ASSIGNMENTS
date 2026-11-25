#Remove duplicate characters
#Take a string and print it with repeated characters removed, keeping the first occurrence.

a = input("Enter the string:").lower()
unique =" "
for ch in a:
    if ch  not in unique:
        unique += ch
print("without duplicates:",unique)        