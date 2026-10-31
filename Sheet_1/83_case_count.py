str = input("Enter a string: ")
case_count = {"uppercase": 0, "lowercase": 0}

for char in str:
    if char.isupper():
        case_count["uppercase"]+=1
    elif char.islower():
        case_count["lowercase"]+=1

print(case_count)