
print("Tip Calculator")
bill_amount = float(input("Total Bill?"))
tip_percent = int(input("what Tip would you like to give?"))

tip_amount = bill_amount * (tip_percent/100)
total_bill = bill_amount + tip_amount


print(f"You should pay: ${total_bill:.2f} JD")
