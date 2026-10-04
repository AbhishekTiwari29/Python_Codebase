string = input("Enter a String: ")
character = input("Enter character: ")
index_no = 0 

for i in string:
    if i == character:
        print(index_no)
        break
    else:
        index_no +=1