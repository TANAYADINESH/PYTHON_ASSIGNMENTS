#Character frequency
#Take a string and print how many times each character appears.

a = input("Enter character:")
freq = {}

for ch in a:
    freq[ch] = freq.get(ch,0)+1
for ch, count in freq.items():
    print(ch, ":", count)
