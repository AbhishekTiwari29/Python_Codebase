p = int(input("Enter Principal: "))
r = float(input("Enter Rate: "))
t = float(input("Enter Time: "))

ci = p*(1+ r/100)**t - p

print(int(ci))

