marks1=int(input("Enter marks in Mathematics"))
marks2=int(input("Enter marks in Physics: "))
marks3=int(input("Enter marks in Chemistry"))
percentage=int(input("Enter percentage: "))

total_Marks=marks1+marks2+marks3
percentage=(total_Marks/300)*100
if marks1>=90 and marks2>=50 and marks3>=70 and percentage>=60:
    print("Eligible for Admission")
else:
    print("Not Eligible for Admission")
