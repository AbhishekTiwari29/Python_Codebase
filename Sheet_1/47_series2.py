x = int(input("Enter X: "))
n = int(input("Enter n: "))
total = 1
for i in range(2,n+1):
    total += (x**i)/i

print(total)