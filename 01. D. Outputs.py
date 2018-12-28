#different ways to print

print("HELLO WORLD")
print("Hello \n\nWorld")
print("Hello \t\t World")

print("Printing without the auto end: ")
print("Hello", end="")
print(" World")

print("Different ways to print concat")
name = "World"
print("Hello", name)
print("Hello {}".format(name))
print("Hello %s" %name)

a = 5
print("%d" %a)
b = 14.123123123123
print("%f" % b)
b = 15.312321231
print("Printf Style: %d %.3f" % (a, b))

b = 10
c = 20
print(a,b,c)
print("{} {} {}".format(a,b,c))
print("{0} {1} {2}".format(a,b,c))
print("{2} {1} {0}".format(a,b,c))
