num=int(input("Enter a number: "))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print("Not a prime number",num)
            break
    else:
        print("It is a prime number",num)
else:
    print("Not a prime number",num)