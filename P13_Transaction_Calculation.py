Pin=int(input("Enter Pin: "))
Account_balance=int(input("Enter balance: "))
Withdrawal_Amount=int(input("Enter Amount: "))

if Pin==1425:
    if  Withdrawal_Amount>0 and Withdrawal_Amount<=Account_balance:
        Account_balance -=Withdrawal_Amount
        print("Transaction Successful")
        print("Amount Withdrawal: ",Withdrawal_Amount)
        print("Remaining balance: ",Account_balance)
    else:
        print("Transaction Failed")
else:
    print("Invalid PIN")