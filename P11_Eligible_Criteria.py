Age=int(input("Enter person age:"))
monthly_income=int(input("Enter person monthly income: "))
Credit_Score=int(input("Enter person credit score: "))

if Age>=21 and Age <=60 and monthly_income>=45000 and Credit_Score >=650:
    print("eligible for loan ")
else:
    print("Not eligible for loan")