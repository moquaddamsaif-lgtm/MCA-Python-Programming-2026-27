while True:
    print("1.Prime\n2.Palindrom\n3.Armstrong\n4.Factorial\n5.Fibonacci Series\n6.Exit")
    ch=int(input("Enter your choice: "))

    if ch==6:
            print("Exit")
            break

    num=int(input("Enter your number: "))

    if ch==1:
        if num>1:
            for i in range(2,num):
                if num%i==0:
                    print(num,"is not a prime number")
                    break
            else:
                 print(num,"it is a prime number")
        else:
                print(num,"it is not a prime number")

    elif ch==2:
        temp=num
        rev=0
        while num>0:
            digit=num%10
            rev=rev*10 +digit
            num=num//10

        if rev==temp:
            print(temp,"it is a palindrom number")
        else:
            print(temp,"Not a palindrom number")

    elif ch==3:
        temp=num
        sum=0
        digits=len(str(num))
        while num>0:
            digit=num%10
            sum+= digit **digits
            num=num//10

        if sum==temp:
            print(temp,"is a Armstrong number")
        else:
            print(temp,"is not a Armstrong number")

    elif ch==4:
        fact=1
        for i in range(1,num+1):
            fact*=i
        print("Factorial of",num,"is",fact)

    elif ch==5:
        a,b=0,1
        for i in range(num):
            print(a)
            temp=a
            a=b
            b=temp+b
        print()

   


