users = {}

while True:
    print("1. Register")
    print("2. login")
    print("3. Exit")
    choice = int(input("Enter Choices: "))

    if choice ==1:
        username = input("Enter Username:" )
        password = input("Enter Password:" )
        if username in users:
            print("User Already Exists")
        else:
            users[username] = password
            print("Registration Successful!")

    elif choice == 2 :
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        if username in users and users[username] == password:
            print("Login Successful!")
        else:
            print("Invalid username & Password")

    elif choice ==3:
        print("Thank You!")
        break
    else:
        print("Invalid Choice!")