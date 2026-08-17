salary = int(input("Enter Salary: "))
hra = (salary*10)/100
da = (salary*5)/100
pf = (salary*3)/100

if  0 <= salary <= 100000 :
    print("K")
    tax =0
elif 1100000 <= salary <= 2000000:
    tax = salary*20/100
elif 500000 <= salary <= 1000000 :
    tax = salary*10/100
elif salary > 2000000:
    tax = salary*30/100
else:
    tax = 0

inHand_salary = salary - hra - da - pf - tax

print(inHand_salary)