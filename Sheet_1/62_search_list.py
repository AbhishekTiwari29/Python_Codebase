l1 = [5,1,2,3,4,5,8,9,6,5,4,45,21,84,54,98,45]
number = 84

for i in l1:
    if i == number:
        print(number, "is Present in the list")
        break
else:
    print(number, "is not present in the list")