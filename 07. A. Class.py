#Classes and objects

class Person:
    def eating(self):
        print("I'm eating")
    def walking(self):
        print("I'm walking")
    def doMath(self, a, b):
        print("The output is: ", a+b)


person1= Person()

person1.walking()
person1.eating()
person1.doMath(5,100)

person2 = Person()
person1.walking()
person1.eating()
person1.doMath(500,100)