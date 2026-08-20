import math
X1 = float(input("Enter X1 : "))
Y1 = float(input("Enter Y1 : "))
X2 = float(input("Enter X2 : "))
Y2 = float(input("Enter Y2 : "))

distance = math.sqrt((X2-X1)**2 + (Y2-Y1)**2)
print(f"Distance is : {distance}")