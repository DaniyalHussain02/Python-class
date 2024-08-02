def discount_october_sundays(day, month, amount):
    if day == "Sunday" and month == "October":
        amount = amount * 0.9  # 10% discount for Sundays in October
    return amount

amount = float(input("Enter the amount: "))
month = input("Enter the Month: ")
day = input("Enter the day: ")
payable_amount = discount_october_sundays(day, month, amount)
print("The Payable amount is:", payable_amount)
