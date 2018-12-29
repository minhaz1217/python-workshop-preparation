#Double underscore in front of a variable or method name means it is private, so outside can't access it directly
class Person:
    def __init__(self, fname, lname):
        self.firstName = fname
        self.__lastName = lname
    def say(self):
        print("My name is ", self.firstName, self.__lastName)

person1 = Person("Minhazul", "Hayat")
person1.say()

print(person1.firstName)
#print(person1.__lastName) #access is not possible
print(person1._Person__lastName) #access is possible like this


class SeeMee:
    def youcanseeme(self):
        return 'you can see me'

    def __youcannotseeme(self):
        return 'you cannot see me'


# Outside class
Check = SeeMee()
print(Check.youcanseeme())
# you can see me
#print(Check.__youcannotseeme())
# AttributeError: 'SeeMee' object has no attribute '__youcannotseeme'

print(Check._SeeMee__youcannotseeme())
# access to any private variables is still possible like this