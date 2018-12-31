dict = { 'name' : "Samani", "age" : 35, "occupation":"student", 450: "daily expence"}

print(dict.get("name"))
print(dict.get("names")) #names isn't a key, so None is returned
try:
    print(dict["names"]) #this throws an error
except:
    print("The key was not found")

print("List of keys: ",dict.keys())
print("List of values: ",dict.values())

print("\nChecking if a key exists")
if( "name" in dict ):
    print("name is found in dict")
else:
    print("it wasn't found")

if( "names" in dict ):
    print("names is found in dict")
else:
    print("names wasn't found")
if( "Samani" in dict ):
    print("names is found in dict")
else:
    print("names wasn't found")
print("\nitems()")
print(dict.items()) # item method outputs list of tuples
print(dict.items()) # item method outputs list of tuples


for key, value in dict.items():
    print("{} -> {}".format(key, value))