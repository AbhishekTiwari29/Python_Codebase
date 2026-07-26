age1 = input("Enter Your 1st Age : ")
age2 = input("Enter Your 2st Age : ")
age3 = input("Enter Your 3st Age : ")

'''
oldest_age = 0

if age1 > age2 and age1 > age3:
    oldest_age = age1
elif age2 > age1 and age2 > age3:
    oldest_age = age2
else : oldest_age = age3
'''

oldest = max(age1, age2, age3)


print(f"Oldest Age is : {oldest} ")
