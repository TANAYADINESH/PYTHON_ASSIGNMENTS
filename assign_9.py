#Experiment No-9-
#Write a program that opens a file and then reads the contents of the file.The Program then should print the contents of the file


file = open("sample.txt", "r")


content = file.read()


print("Contents of the file:")
print(content)


file.close()