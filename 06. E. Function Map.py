#Function with map

myList = [1,2,3,4,5]
def square(a):
    return a*a

squiredList = list(map(square, myList))
print(squiredList)

names = ["Shuvo", "Tamanna", "Orpon", "Nabila"]
def sayHello(a):
    return ("Hello "+  a)

batchSayHello = list(map(sayHello, names))
for i in batchSayHello:
    print(i)