hours = float(input("hours : "))
minutes = float(input("minutes : "))

hours = hours % 12

hours = (30*hours) + (0.5*minutes)
minutes = minutes * 6

difference = abs(hours - minutes)
angle = min(difference , 360-difference)

print(angle)