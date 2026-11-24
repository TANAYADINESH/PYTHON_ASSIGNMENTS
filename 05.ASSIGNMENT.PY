# Student Average Calculator

n = int(input("Enter the number of students: "))

total_class = 0

for i in range(n):
    print("\nStudent", i + 1)

    total = 0

    for j in range(5):
        marks = float(input("Enter marks for test " + str(j + 1) + ": "))

        total = total + marks

    average = total / 5

    print("Average of Student", i + 1, "=", average)

    total_class = total_class + total

overall_average = total_class / (n * 5)

print("\nOverall Class Average =", overall_average)