myFile = open("file.txt", "r")
content = myFile.read()
print(content)
myFile.close() #remember to close the file

#myFile = open("open.txt", "r") #this will thorw an error as the file doesn't exists

try:
    myFile = open("open.txt", "r")
except:
    print("Couldn't find the file")
