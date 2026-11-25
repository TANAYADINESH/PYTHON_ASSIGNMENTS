#Word frequency
#Take a sentence and print how many times each word appears, ignoring case.
s = input("Enter a sentence: ").lower()
count = {}
for w in s.split():
    count[w] = count.get(w, 0) + 1
for w, c in count.items():
    print(w, "->", c)