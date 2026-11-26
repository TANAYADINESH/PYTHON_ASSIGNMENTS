#File handling: count lines, words, characters 
#Read sample.txt and print the number of lines, words and characters. Then append a new line typed by the user and print the file line by line with line numbers.

with open("sample.txt","r")as f:
    content = f.read()

print("Lines:", len(content.splitlines()))
print("Words:", len(content.split()))
print("characters:", len(content))

new_line = input("Enter new line:")
with open ("sample.txt","a")as f:
    for i, line in enumerate(f, start=1):
        print(i, ":", line.strip())
