# this file is only to reset the file to default for the other lectures
with open("file.txt", "w") as myFile:
    myFile.write("First Line\n1\n2\n3\nLast Line\n")

with open("file.txt", "r") as myFile:
    print(myFile.read())