num=int(input("Enter a integer"))
sum=0
product=1
temp=num
while num>0:
    digit=num%10
    sum=sum+digit
    product=product*digit
    num=num//10

print("Original Number =", temp)
print("Sum of digit=",sum)
print("Product of digit=",product)