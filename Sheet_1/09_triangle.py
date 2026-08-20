angle1= int(input("Enter Angle1: "))
angle2= int(input("Enter Angle2: "))
angle3= int(input("Enter Angle3: "))

total = angle1 + angle2 + angle3
if angle1 >0 and angle2 > 0 and angle3 > 0 and total == 180:
    print("This Forms a Triangle")
else:
    print("This does not form a Triangle")