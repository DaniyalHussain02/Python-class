def check_temperature(temp):
    if temp == 98.6:
        print("Normal")
    else:
        print("Temperature:",temp)

while True:
    temperature = float(input("Enter the temperature of the patient in Fahrenheit: "))
    check_temperature(temperature)
    
    decision = int(input("If you want to continue, press 1; otherwise, press 0: "))
    if decision == 0:
        break
