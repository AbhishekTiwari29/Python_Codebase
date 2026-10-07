l1 = list(map(int, input("Enter Number for list_1: ").split()))
l2 = list(map(int, input("Enter Number for list_2: ").split()))

l3 = []
for i in l1:
    l3.append(i)
for i in l2:
    l3.append(i)
print("Merged_list", l3)