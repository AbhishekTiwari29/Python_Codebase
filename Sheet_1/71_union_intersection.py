l1 = list(map(int,input("Enter Numbers: ").split()))
l2 = list(map(int,input("Enter Numbers: ").split()))

l3 =  set(l1).intersection(set(l2))
l4 =  set(l1).union(set(l2))

print("Intersection: ",list(l3))
print("Union: ",list(l4))