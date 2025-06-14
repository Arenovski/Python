Medical_Cause = str(input("Do you have a medical cause Y or N"))
Attendence = int(input("What is your attendence rate"))

if Medical_Cause == "Y":
    print("You are allowed")
else:
    if Attendence >=75:
        print("You're allowed")
    else:
        print("Not allowed")