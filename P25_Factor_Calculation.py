num=int(input("Enter a number:"))
count=0

print("Factors of",num,"are:")

for i in range(1,num+1):
    if num%i==0:
        print(i)
        count+=1

print("Total number of factors=",count)

