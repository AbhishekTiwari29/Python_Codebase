year = int(input("Enter Year : "))

if year % 4 == 0 and year % 100 != 0:
    print("leap Year")
elif year % 400 == 0:
    print("leap Year")
else:
    print("Not a Leap Year")