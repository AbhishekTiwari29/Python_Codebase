number = input("Enter Number: ")
n = len(number)
result = 0
for i in number:
    result += int(i)**n
print(result)
if int(number) == result:
    print(f"{number} is Armstrong number")
else:
    print(f"{number} is not Armstrong number")