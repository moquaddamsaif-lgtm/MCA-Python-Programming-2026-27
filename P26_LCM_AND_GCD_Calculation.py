x=int(input("Enter 1st  integer: "))
y=int(input("Enter 2nd integer: "))

gcd=1
for i in range(1,min(x,y) +1):
    if x%i==0 and y%i==0:
        gcd=i


lcm=(x*y)//gcd

print("GCD =",gcd)
print("LCM = ",lcm)

