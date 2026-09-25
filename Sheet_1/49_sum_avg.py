total = 0
count = 0
n = int(input("Enter n: "))
while n != 0:
    total += n
    count +=1
    n = int(input("Enter n: "))

if count==0:
    print(0)
else:
    avg = total/count
    print(avg)
