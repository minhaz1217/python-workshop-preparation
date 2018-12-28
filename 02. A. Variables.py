var_int = 10
var_float = 123.123123123
var_long = 321321321321321321321321321321321321321321321321
var_char = 'A'
var_string = "HELLO WORLD"
var_bool = True #notice the First letter is in upper case
var_null = None

print("Integer: ", var_int)
print("Float: ", var_float)
print("Big Integer: ", var_long)
print("Char: ", var_char)
print("Float: ", var_string)
print("Boolean: ", var_bool)
print("None: ", var_null)

myList = [1,2,3,4] #this is a list
mySet = {10,20,30,40,40,30} # this is a set so any duplicates will get removed
print(myList, type(myList))
print(mySet, type(mySet))
print(myList[0])
print("Length of the set: ", mySet.__len__())

myList.append(5)
print(myList)
mySet.add(5)
print(mySet)

myRandomList = [1, "HI", 2.3333]
print(myRandomList, type(myRandomList))

#Initializing a list without any value in it
myList2 = list()
print(myList2, type(myList2), len(myList2), myList2.__len__())


'''
There are only 4 major data types
1. int 
2. float
3. str
4. list
'''
