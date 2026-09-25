    x = int(input("Enter X: "))
    n = int(input("Enter n: "))
    formula = (x - 1)/x
    total = formula

    for i in range(2,n+1):
        total += 1/2*(formula)**i

    print("Sum =",total)