English = int(input("What were your marks for english"))
Maths = int(input("What were your marks for Maths"))
History = int(input("What were your marks for History"))
Science = int(input("What were your marks for Science"))
PE = int(input("What were your marks for PE"))
total = English+Maths+History+Science+PE
average = total/5
if average>=91 and average<=100:
    print("Your Grade is A")
elif average>=80 and average<=90:
    print("Your grade is B")
elif average>=69 and average<=79:
    print("Your grade is c")
elif average>=58 and average<=68:
    print("Your Grade is D")
elif average>=47 and average<=57:
    print("Your grade is E")
elif average<=1:
    print("Your Grade is -----------------------------z")
else:
    print("Invalid Input")