myTuple = ()
print(type(myTuple))
myTuple = ("tomato", "potato", 30,4.55555)
print(myTuple)
print(len(myTuple))
print(myTuple[0])
print(myTuple[1])
print(myTuple[1:3])

for i in myTuple:
    print(i)

print("\nChanging")

try:
    myTuple[0] = "ornage"
except:
    print("Problem occured")

myTuple = myTuple + ("potato", 'dog')
print(myTuple)
print("Count potato: ", myTuple.count("potato"))
print("Count dog: ", myTuple.count("dog"))

dogIndex = myTuple.index("dog")
print("Find dog: ", myTuple.index("dog"))
try:
    myTuple.index("dogs")
except:
    print("Couldn't find dogs")