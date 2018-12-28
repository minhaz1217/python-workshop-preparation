
print("CONTINUE - Printing from 1 to 10 without 5")
for a in range(1,11):
    if(a == 5):
        continue
    print(a)

print("BREAK - Printing from 1 to 10 but stopping if 5 is found")
for a in range(1,11):
    if(a == 5):
        break
    print(a)

print("PASS - It is a place holder it does absolutely nothing")
for a in range(1,11):
    if(a == 5):
        print("HI")
        pass
    print(a)
