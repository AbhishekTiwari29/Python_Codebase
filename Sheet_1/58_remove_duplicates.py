l1 = [1,2,4,5,8,4,1,2,4,5,1,2,14,1,2,4,2]
l2 =[]
for i in l1:
    if i not in l2:
        l2.append(i)

print(l2)