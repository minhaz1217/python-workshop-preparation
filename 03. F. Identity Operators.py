#Identity operators
#with is and is not operator we can check if two values are located in the same part of the memory
a = 5
b = 5
print("Inputs: \n a = {} \n b = {}".format(a,b))
print("a is b Result: ",a is b)
print("a is not b Resule: ", a is not b)
a = [1,2,3]
b = [1,2,3]
print("Inputs: \n a = {} \n b = {}".format(a,b))
print("a is b Result: ",a is b)
print("a == b Result: ", a == b)
# even though their value is same but this produces false because they are not in the same memory space