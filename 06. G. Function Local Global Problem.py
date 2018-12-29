#Global and local variable problem

a = 10

print("Before Change: ", a)
def changeValue(b):
    a = b;

changeValue(100)
print("After Change: ", a)
'''
The value didn't change because the a inside the function is the new a and that is the on that's being chnaged.
'''



# The fix

a = 10
print("Before Change: ", a)
def changeValue2(b):
    global a
    a = b
changeValue2(100)
print("After Change: ", a)


