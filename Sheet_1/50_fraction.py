num = int(input("Enter numerator: "))
den = int(input("Enter denominator: "))

a = num
b = den

while b != 0:
    a, b = b, a % b

gcd = a

num = num // gcd
den = den // gcd

print(num, "/", den)