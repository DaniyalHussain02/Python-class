def discount(price):
    if price == 500:
        price = price - (price * 0.05)
    return price

while True:
    total_price = int(input("Enter the total price of your items: "))
    updated_price = discount(total_price)
    print(f"Price after Discount: {updated_price}")
    
    decision = int(input("If you want to continue, press 1; otherwise, press 0: "))
    if decision == 0:
        break
