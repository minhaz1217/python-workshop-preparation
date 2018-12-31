dict = {"name": "Raka","age" : 10}
print(dict)
try:
    print(dict["name"])
except:
    print("Error occured")
else:
    print("Found Successfully")

try:
    print(dict["country"])
except:
    print("Error occured")
else:
    print("Successful")

#how to avoid and exception
try:
    print(dict["country"])
except:
    pass
