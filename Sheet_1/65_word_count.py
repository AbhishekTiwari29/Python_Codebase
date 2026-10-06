string = input("Enter String: ")
count = 0
words = string.split()

for i in words:
    count +=1

print("Total Words in String:", count)