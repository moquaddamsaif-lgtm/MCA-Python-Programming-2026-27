n=int(input("Enter number of terms: "))
a,b=0,1
sum=0

print("Fibonaaci series: ")

for i in range(n):
    print(a)
    sum+=a
    temp = a
    a = b
    b = temp + b