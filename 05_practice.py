#Student marks: highest, lowest, pass/fail
#For n students and 5 tests each, print each student's average (2 decimals) with Pass/Fail (pass is 40 or more),then the class average, highest and lowest.

n = int(input("Enter number of students:"))
marks = []
total_class = 0

for i in range(n):
    print("\nStudent",i+1)
    total = 0
    for j in range(3):
        mark = float(input("Enter marks for test"+str(j+1)+":"))
        total = total + mark
        average = total/3
    marks.append(average)
    total_class = total_class + total

class_average = total_class / (n * 3)
highest = max(marks)
lowest = min(marks)

print("\nClass Average:", round(class_average, 2))
print("Highest:", highest)
print("Lowest:", lowest)