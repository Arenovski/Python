string = str(input("Enter a word"))
string2 = ("")
for i in string:
    string2 = i+string2

print("The origanal word:", string)
print("The reversed word: ", string2)