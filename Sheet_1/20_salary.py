salary = int(input("Enter Salary: "))
hra = (salary*10)/100
da = (salary*5)/100
pf = (salary*3)/100

inHand_salary = salary - hra - da - pf 

if  0 <= salary <= 100000 :
    print("K")
elif 1100000 <= salary <= 2000000:
    print(inHand_salary - (inHand_salary*20)/100)
elif 500000 <= salary <= 1000000 :
    print(inHand_salary - (inHand_salary*10)/100)
else:
    print(inHand_salary - (inHand_salary*30)/100)