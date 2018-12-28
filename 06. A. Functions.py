#Functions
def sayHi():
    print("Hi there, Welcome")

sayHi();


def sayHello(name):
    print("Hello {}, welcome to our workshop".format(name))


yourName = str(input("Enter your name: "))
sayHello(yourName)


def printSum(a, b, c):
    print(a+b+c)
printSum(5,10,15)

