num=int(input("Enter an integer"))
temp=num
sum=0

digits=len(str(num))
while num>0:
    digit=num%10
    sum=sum+digit**digits
    num=num//10

if sum==temp:
    print("It is Armstrong number",temp)
else:
    print("Not a Armstrong number",temp)