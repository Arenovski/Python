cp = int(input("What was the cost price: "))
sp = int(input("What was the selling price: "))

if(cp<sp):
    profit = sp - cp
    print("You have profit $",profit)
else:
    loss = cp - sp
    print("You have a loss $",loss)
