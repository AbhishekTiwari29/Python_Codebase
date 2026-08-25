num = int(input("Enter Number: "))

if num < 2:
    print("Not Prime")
else:
    for i in range(2 , num):
        if num % i  == 0:
            print("not prime")
            break
    else:
            print(" prime")