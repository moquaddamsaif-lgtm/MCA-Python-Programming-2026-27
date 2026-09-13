percentage = int(input("Enter Student percentage: "))

if percentage < 0 or percentage > 100:
    print("Invalid percentage! Percentage should be between 0 and 100.")
else:
    if percentage >= 90:
        grade = 'A'
    elif percentage >= 80:
        grade = 'B'
    elif percentage >= 70:
        grade = 'C'
    elif percentage >= 60:
        grade = 'D'
    elif percentage >= 50:
        grade = 'E'
    else:
        grade = 'F'

    print("Grade:", grade)
