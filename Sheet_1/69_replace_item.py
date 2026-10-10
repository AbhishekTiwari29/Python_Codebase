l1 = [1,2,3,4,5,6,7,8,9]
remove_number = int(input("Enter number we remove: "))
add_number = int(input("Enter number we add: "))

for i in range(len(l1)):
    if l1[i] == remove_number:
        l1[i] = add_number

print(l1)