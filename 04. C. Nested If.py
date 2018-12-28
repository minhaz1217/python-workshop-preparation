#Nested if

a = int(input("Enter a number: "))

if(a < 20):
    if(a%2 == 0):
        print("Input is LESS than 20 and EVEN")
    else:
        print("Input is LESS than 20 and ODD")
else:
    if(a%2 == 1):
        print("Input is GREATER than 20 and ODD")
    else:
        print("Input is GREATER than 20 and EVEN")
