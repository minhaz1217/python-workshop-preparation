message = "The name of my country is Bangladesh"

print("Message before: ", message)
print("Message after: ", message.replace('my', "our"))
print(message.replace("a", "i"))

splitMessage = message.split(" ")
print(splitMessage)
print("Message: ", message)
newMessage = "       Bangladesh         "
print("New message: ", newMessage)
print("Stripping:", newMessage.strip())
print("Stripping Beginning:", newMessage.lstrip(), "HERE")
print("Stripping End:", newMessage.rstrip(),"HERE")
print(message.strip("desh"))
print(message.strip("The")) #strip can only remove things from beginning or from end

country = "Bangladesh"
print(country.ljust(20))
print(country.rjust(20))
print(country.center(20))
print(country.center(20, '*'))