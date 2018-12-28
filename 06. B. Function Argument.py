
print("Default argument")
def add(a,b,c=1):
    print(a+b+c)

add(5,10,15)
add(5,10)

print("Keyword argument")

add(c = 5, b = 10, a = 100)