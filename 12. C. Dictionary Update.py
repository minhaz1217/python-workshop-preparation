dict = { 'name' : "Samani", "age" : 35, "occupation":"student", 450: "daily expence"}
print(dict)
dict["country"] = "Bangladesh"
print(dict)

print("Name before update: ", dict["name"])
dict["name"] = "Lamia"
print("Name after update: ", dict["name"])
print("\nUpdate")
dict.update( { "age" : 28, "country" : "japan" } ) #in update method put the key and value pair that you want to update.
print(dict)

print("\nRemoving")
del(dict["name"])
print(dict)
print("\nPop : ")
print(dict.pop("country"))
print(dict)
print("Pop item: ", dict.popitem()) #pop item just removes the first item from the dictionary
print(dict)
print("Pop item: ",dict.popitem())
print(dict)
dict.clear()
print("Size: ", len(dict), "Dictionary: ",dict)
secondDictionary = { 'name' : "Laana", "age" : 21, "occupation":"student", 450: "daily expence"}
print(secondDictionary)
print("Dictionary: ", secondDictionary.copy())
