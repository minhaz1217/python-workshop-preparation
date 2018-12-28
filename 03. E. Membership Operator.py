#Membership operators
a = "Hello World"
b = "World"

print("Inputs: \n a = {} \n b = {}".format(a,b))
print("a in b Resule: ",a in b)
print("b in a Resule: ",b in a)

a = [1,2,3,4]
b = 1
print("Inputs: \n a = {} \n b = {}".format(a,b))
print("b in a Result: ", b in a)
b = [1]
print("Inputs: \n a = {} \n b = {}".format(a,b))
print("b in a Result: ", b in a) # this outputs false because b is a list but members in a are integers, if a had a value like [1] then the outputs will be true

