#function overloading
def add(a, b,c= None, d = None):
    if(c == None and d == None):
        print("Double", a+b)
    elif(d == None):
        print("Triple:", a+b+c)
    else:
        print("Quadruple:", a+b+c+d)
add(5,10)
add(5,10,15)
add(5,10,15,20)

#normal C/Java style overloading based on the parameter isn't possible in python