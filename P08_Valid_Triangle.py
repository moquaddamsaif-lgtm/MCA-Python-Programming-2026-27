a=int(input("Enter 1st side: "))
b=int(input("Enter 2nd side: "))
c=int(input("Enter 3rd side: "))

if a+b>c and a+c>b and b+c>a:
    print("Valid Triangle")
    if a==b==c :
       print("Equilateral Triangle")
    elif a==b or a==c or b==c:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Not a Valid Triangle")    