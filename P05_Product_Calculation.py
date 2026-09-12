price1=int(input("Enter price of product1:"))
quantity1=int(input("Enter quantity of product 1:"))


price2 = int(input("Enter price of product 2: "))
quantity2 = int(input("Enter quantity of product 2: "))

price3 = int(input("Enter price of product 3: "))
quantity3 = int(input("Enter quantity of product 3: "))

subtotal = (price1 * quantity1) + (price2 * quantity2) + (price3 * quantity3)

discount=(subtotal*20) /100

gst = (subtotal * 5) / 100

final_amount = subtotal + gst - discount

print("Subtotal:", subtotal)
print("Discount:", discount)
print("GST:", gst)
print("Final Payable Amount:", final_amount)