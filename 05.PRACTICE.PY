#Count vowels and consonants
#Take a string and print the number of vowels and consonants

a = input("Enter a string: ").lower()
vowels = consonants = 0

for ch in a:
    if ch.isalpha():
        if ch in "aeiou":
            vowels+=1
        else:
            consonants+=1
print("Vowels:",vowels)
print("Consonants",consonants)                
