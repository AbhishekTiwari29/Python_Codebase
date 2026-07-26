while True:
    number = input("Enter 4 Digit Number : ")
    if len(number) == 4 and number.isdigit():

        result = ""
        number = int(number)

        while number > 0:
            result += str(number%10)
            number //= 10
        print((result))
        break
    else:
        print("Please Enter 4 Digit Number")