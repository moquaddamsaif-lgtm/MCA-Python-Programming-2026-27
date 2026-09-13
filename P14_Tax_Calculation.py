income=int(input("Enter annual income: "))

if income<60000:
    tax=(income*5)/100
elif income >= 60000 and income < 150000:
    tax = (income * 10) / 100
elif income >= 150000 and income < 300000:
    tax = (income * 20) / 100
else:
    tax = (income * 30) / 100

print("Annual Income:",income)
print("Tax payable",tax)
