n = int(input("Enter Number: "))
total = 0
product = 1 
for i in range(1,n+1):
    product *= i
    total += i/product

print(total)