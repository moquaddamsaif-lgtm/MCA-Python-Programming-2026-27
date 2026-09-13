num=int(input("Enter a Integer:"))
if num==0:
    print("Number is Zero")
elif num>0:
    print("Number is positive")
    if num%2==0:
        print("Even number")
    else:
        print("Odd number")
else:
    print("Number is negative")
