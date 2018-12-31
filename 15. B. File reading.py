print("\nAfter writing")
with open("file.txt", "r") as myFile:
    print(myFile.read())

print("\nRead with parameter")
myFile = open("file.txt", "r")
print(myFile.read(2)) #just read 2 letters
print(myFile.read(7)) #read next 7 letters
print(myFile.tell()) # tell gives us where the current pointer/cursor is
myFile.seek(2,0) #seek(position, offset) the positon and the offset
print(myFile.read()) #now  the read starts from 2'th position
'''
0 means relative to file's start
1 means relative to current position
2 means relative to file end position
'''
myFile.close()