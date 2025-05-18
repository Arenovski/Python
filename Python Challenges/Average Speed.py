Speed1 = int(input("Enter your first speed:  "))
Speed2 = int(input("Enter your second speed:  "))
Speed3 = int(input("Enter your third speed:  "))
average = (Speed1 + Speed2 + Speed3)/3
print("The average speed is", average)
if average>Speed1 and average>Speed2 and average>Speed3:
    print("%d is faster than %d, %d, %d"%(average, Speed1, Speed2, Speed3))
elif average>Speed1 and average>Speed2:
    print("%d is faster than %d, %d"%(average, Speed1, Speed2))
elif average>Speed1 and average>Speed3:
    print("%d is faster than %d, %d"%(average, Speed1, Speed3))
elif average>Speed3 and average>Speed2:
    print("%d is faster than %d, %d"%(average, Speed3, Speed2))
elif average>Speed1:
    print("%d is faster than %d"%(average, Speed1))
elif average>Speed2:
    print("%d is faster than %d"%(average, Speed2))
elif average>Speed3:
    print("%d is faster than %d"%(average, Speed3))
else:
    print("Invalid Input")