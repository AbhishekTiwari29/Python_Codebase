number = int(input("Enter Your Number: "))
total = 1

for i in range(number,0,-1):
    total *= i
print(total)