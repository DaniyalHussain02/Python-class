def discount(day,month,amount):
    if(day=="Sunday" or month=="october"):
       amount=amount*0.9
    return amount


amount = float(input("Enter the amount: "))
month = input("Enter the Month: ")
day = input("Enter the day: ")
payable_amount = discount(day, month, amount)
print("The Payable amount is:", payable_amount)