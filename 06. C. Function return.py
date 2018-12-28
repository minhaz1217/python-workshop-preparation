def sum(a, b ,c):
    return a+b+c
temp = sum(5,10,20)
print(temp)


def maxMin(a , b):
    if(a>b):
        tempMax = a
        tempMin = b
    else:
        tempMax = b
        tempMin = a
    return tempMax, tempMin
myMax, myMin = maxMin(5,10)
print("Max", myMax, "Min", myMin)
myMax, myMin = maxMin(100,10)
print("Max", myMax, "Min", myMin)