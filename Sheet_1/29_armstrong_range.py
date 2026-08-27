number = input("Enter Number: ")
n = len(number)
result = 0
total = 0
for i in number:
    result += int(i)**n
print(result)
if int(number) == result:
    total += 1