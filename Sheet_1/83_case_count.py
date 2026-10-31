def count_case(s):
    case_count = {"uppercase": 0, "lowercase": 0}

    for char in s:
        if char.isupper():
            case_count["uppercase"]+=1
        elif char.islower():
            case_count["lowercase"]+=1
    return case_count
text = input("Enter a String")
print(count_case(text))