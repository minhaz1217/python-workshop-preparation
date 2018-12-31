food = {"apple", "orange", "banana"}
print(food)
print("\nAdding")
print(food)
food.add("mango")
print(food)
print("\nremove()")
food.remove("orange")
print("after remove: ",food)

food.discard("banana")
print("after dicard: ", food)
#food.remove("oranges")
food.discard("oranges")
'''
remove(name) dicard(name) both does the same thing, but remove can throw an error while dicard doesn't thorw an error
'''

print("\npop()")
print("Pop: ", food.pop())
print(food)

print("\nUpdating")
food = {"apple", "orange", "banana"}
print(food)
food.update({"malta", "grape"})
print(food)
food.clear()
print(food)