l1 = [1, 2, 3, 4, 5]

ascending = True

for i in range(len(l1) - 1):
    if l1[i] > l1[i + 1]:
        ascending = False
        break

if ascending:
    print("List is in ascending order")
else:
    print("List is not in ascending order")