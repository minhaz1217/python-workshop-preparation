#Built in functions
#print(math.pow(3,2))
print("Absolute: ",abs(-1))
print("Power: ", pow(2,2))
myList = [5,2,3,1,4,2]
print("Type: ", type(myList))
print("Length: ", len(myList))
print("The List: ", myList)
print("Reverse: ",list(reversed(myList)))
print("Sum: ", sum(myList))
print("Max: ", max(myList))
print("Min: ",min(myList))
mySortedList = sorted(myList)
print("Sorted: ", mySortedList)


print("Generating Numbers: ", list(range(4)))
print("Generating numbers: ", list(range(1,11)))
print("Generating Numbers with increment: ", list(range(1,11,4)))
print("Rounding down: ", round(1.2323))
print("Rounding up: ",round(1.56))
print("As String: ", str(myList))