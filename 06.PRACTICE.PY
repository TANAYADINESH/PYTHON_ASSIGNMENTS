#Reverse word and reverse each word 
#Take a sentence . Print the words in reverse order ,then each word reversed.

a = input("Enter the sentence:").lower()

words= a.split()
print("Reversed order:"," ".join(words[::-1]))
print("reversed each word:"," ".join(w[::-1]for w in words))