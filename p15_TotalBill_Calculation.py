mobile_data = int(input("Enter your mobile data usage in GB: "))

if mobile_data <= 2:
    total_bill = mobile_data * 50   
elif mobile_data <= 10:
    total_bill = mobile_data * 40
elif mobile_data <= 30:
    total_bill = mobile_data * 30
else:
    total_bill = mobile_data * 20

print("Data Usage:", mobile_data)
print("Total Bill:", total_bill)
