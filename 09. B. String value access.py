country = "Bangladesh"
print(country[0])
print(country[1])
print(country[2])

print("Access from back: ", country[-1])
print("Access from back: ", country[-2])
for i in country:
    print(i, end="")
print("")
print("String size: ", len(country))
print("%s is my the country I live in." %country)

print("Back cut 1: ",country[:1])
print("Back cut 2: ",country[:2])
print("Back cut 3: ",country[:3])
print("Front cut 2: ",country[2:])
print("Front cut 4: ",country[4:])
print("Sub string cut: ",country[0:4])
print("Sub string cut: ",country[1:4])
print("Sub string cut: ",country[1:-1])
print("Sub string cut: ",country[7:-1])