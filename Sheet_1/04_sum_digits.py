while True:
    digit = input("Enter 3  Digit Number : ")
    sum = 0

    if len(digit) == 3 and digit.isdigit():
        for i in digit:
            sum += int(i)
        print(f"SUM OF NUMBERS OF DIGITS : {sum} ")
        break
    else:
        print("Please Enter 3 digit No.")