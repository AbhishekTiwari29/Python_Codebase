l1 = list(map(int,input("Enter numbers: ").split()))
even_list = []
odd_list = []

for i in l1:
    if i % 2 ==0:
        even_list.append(i)
    else:
        odd_list.append(i)

print("EVEN list: ", even_list)
print("ODD list: ", odd_list)