units = int(input("Enter electricity units consumed: "))
bill = 0

if units <= 100:
    bill = units * 1.50
elif units <= 200:
    bill = (100 * 1.50) + (units - 100) * 7
elif units <= 300:
    bill = (100 * 1.50) + (100 * 7) + (units - 200) * 10
else:
    bill = (100 * 1.50) + (100 * 7) + (100 * 10) + (units - 300) * 12

print("Total electricity bill: ₹", bill)
