string = input("Enter String: ")
reverse = ""

for i in string:
    reverse = i+reverse

if string == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")