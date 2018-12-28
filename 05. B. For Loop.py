#for loop

print("Default for")
for a in range(10): #It goese from 0 to end -1
    print(a)

print("Printing number from 1 to 10")
for a in range(1,11): #It goes from start to end-1
    print(a)


print("Increment by 2")
for a in range(1,11, 2):
    print(a)

print("Printing list")
fridge = ["Apple","Orange", "Banana"]
for food in fridge:
    print("I'll eat {} after this.".format(food))
