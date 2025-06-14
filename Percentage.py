amount = int(input("Enter the Amount you want to withdraw"))
note1 = amount//100
note2 = (amount%100)//50
note3 = ((amount%100)%50)//10
print("Notes of Hundred Dollars",note1)
print("Notes of 50 Dollars", note2)
print("Notes of 10 Dollars", note3)