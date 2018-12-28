#Loop with else

for i in range(1,6):
    print(i)
else:
    print("The loop has finished successfully")

#a = int(input("Enter starting point: "))
#b = int(input("Enter ending point: "))
#difference between the two
for i in range(1,6):
    print(i)
print("The loop has finished successfully")


#We can detect a break without setting a flag
for i in range(1,11):
    if(i == 5):
        break
    print(i)
else:
    print("The loop has finished successfully")
