string = input("Enter String: ")
character = input("Enter Character: ")
count = 0

for i in string:
    if i == character:
        count +=1

print(count)