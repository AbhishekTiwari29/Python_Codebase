x = int(input("Enter X: "))
formula = (x - 1)/x
total = formula

for i in range(2,8):
    total += 1/2*(formula)**i

print("Sum =",total)