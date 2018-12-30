message = "The name of my country is Bangladesh"
print(message.find("Bangladesh"))
print(message.find("are"))
print(message.count("is"))
print(message.count("a"))
print(message.find("is"))
try:
    print(message.index("are"))
except:
    print("Not found")