email = input("Enter Username: ")

username = []
for char in email:
    if char != '@':
        username.append(char)
    else:
        break

print("".join(username))