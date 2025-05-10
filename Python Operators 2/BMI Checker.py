weight = float(input("How much do you weigh:  "))
height = float(input("What is your height:  "))

BMI = weight/(height/100)**2

print("You BMI is", BMI)
if BMI<=18.5:
    print("You're under weight")
elif BMI>18.5 and BMI<24.9:
    print("You're healthy")
elif BMI>25 and BMI<29.9:
    print("You're over weight")
elif BMI>30:
    print("You're obese")
else:
    print("You're severly obese")