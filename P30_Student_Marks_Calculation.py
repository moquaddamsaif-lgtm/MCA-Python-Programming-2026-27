n = int(input("Enter number of students: "))
marks_list = []
total = 0

for i in range(n):
    print("Enter marks of student", i+1, ":")
    m = int(input())
    marks_list.append(m)
    total += m

    if m >= 40:
        print("Student PASSED")
    else:
        print("Student FAILED")

    if m > 75:
        print("Student scored ABOVE 75%")

avg = total / n
print("\nClass Average:", avg)
print("Highest Marks:", max(marks_list))
print("Lowest Marks:", min(marks_list))
