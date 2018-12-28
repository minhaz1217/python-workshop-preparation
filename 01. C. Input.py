#Normal input
a = int(input())
print("THIS IS WHAT YOU INSERTED: " , a)

#Input with a message
b = str(input("Enter your name: "))
print("Hello There {}, Welcome to our workshop".format(b))


#inputting 2 inputs at the same time
#c ,d = int(input()), int(input())

#or
c ,d = input().split()
print("This is what i got {} for input 1 and {} for input 2".format(c,d))