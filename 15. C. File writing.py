myFile = open("file.txt", "r")
content = myFile.read()
print(content)
myFile.close() #remember to close the file

myFile = open("file.txt", "a") #a means append, so the write command will enter the things at the end of the file
myFile.write("I've wrote this line")
myFile.close()
print("\nAfter writing")
with open("file.txt", "r") as myFile:
    print(myFile.read())

myFile = open("file.txt", "w") # the w flag will replace everythin of that file
myFile.write("Wrote this second line")
myFile.close()

print("\nAfter writing")
with open("file.txt", "r") as myFile:
    print(myFile.read())

# the a and w flag will open new file if the file isn't present in the directory