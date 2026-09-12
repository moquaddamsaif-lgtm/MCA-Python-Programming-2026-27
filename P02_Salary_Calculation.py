salary = float(input("Enter your Salary: "))

DA = salary * 10 / 100
HRA = salary * 20 / 100
gross_salary = salary + DA + HRA
tax_deduction = gross_salary * 5 / 100
net_salary = gross_salary - tax_deduction

print("DA:", DA)
print("HRA:", HRA)
print("Gross Salary:", gross_salary)
print("Tax Deduction:", tax_deduction)
print("Net Salary:", net_salary)