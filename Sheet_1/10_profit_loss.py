cost_price = int(input("enter cost price : "))
selling_price = int(input("enter selling price : "))

difference = selling_price - cost_price

if difference > 0:
    print(f"Profit of : {difference}")
elif difference < 0:
    print(f"Loss of : {abs(difference)}")
else:print("No Loss No Profit")