import math

r = float(input("enter your radius :"))
h = float(input("enter your height :"))

volume = math.pi * r**2 * h
volume_litre = volume/1000
cost= volume_litre * 40

print(f"Milk Capacity = {volume_litre:.2f} litres")
print(f"Total Cost = ₹{cost:.2f}")