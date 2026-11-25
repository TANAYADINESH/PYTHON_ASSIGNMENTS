#Anagram check
#Take two words and check whether they are anagrams, ignoring case.

a = input("Enter first word:").lower()
b = input("Enter second word:").lower()

if sorted(a)==sorted(b):
    print("Anagram")
else:
    print("not a anagram")    