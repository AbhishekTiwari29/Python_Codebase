l1 = [1,48,7,4,1,5,3,8,4,5,6]
l2 = []

for i in range(len(l1)-1):
    for j in range(len(l1)-1):
        if l1[j]>l1[j+1]:
            temp = l1[j+1]
            l1[j+1]= l1[j]
            l1[j] = temp

print(l1)