myList = ["onion", "potato", "ginger", "cucumber", "carrot"]
print(myList)
myList[0] = "rice"
print(myList)
myList.append("banana")
print(myList)
myList.insert(1,"orange") #insert(index, value)
print(myList)
myList.extend(["beef", "fish", "chicken"])
print(myList)

myList = ["onion", "potato", "ginger", "cucumber", "carrot"]
protin = ["beef", "fish", "chicken"]
myList = myList + protin
print(myList)

protin.remove("beef")
print(protin)
protin = ["beef", "fish", "chicken"]
print(protin)
print("Pop: ",protin.pop())#pop removes the last item and returns it
print(protin)
protin = ["beef", "fish", "chicken"]
protin.__delitem__(1) #deleting the index 1, fish
print(protin)
del(protin[0]) #deleting the 0'th item
print(protin)