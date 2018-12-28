
myList = [1,2,3,4,5,6,7,8]

def takeEvensOnly(x):
    if(x%2 == 0):
        return True
    else:
        return False

findAllEven = list( filter(takeEvensOnly, myList ))
print(findAllEven)


#now find all odd with the filter function