num = input("Enter your number: ")

n = len(num)
int_num = int(num)
total = 0 

if n == 4:
    for i in num:
        i = int(i)**n
        total += i
    if total == int_num:
            print(f"{int_num} is narcissist number ")
    else:
            print(f"{int_num} is not narcissist number")
else:
    print("ENTER only 4 Digit Number")
