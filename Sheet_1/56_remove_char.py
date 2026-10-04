string = input("Enter String: ")
character = input("Enter Character: ")
new_string = ""
for i in string:
    if i == character:
        continue
    else:
        new_string +=i
print(new_string)