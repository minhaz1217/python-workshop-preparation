#Class members

class Person:
    def eating(self):
        print("I'm eating")
    def sleeping(self):
        print("I'm sleeping")
    def doMath(self, a, b):
        print("The output is: ", a+b)

    def setMyName(self, name):
        self.name = name
    def sayHello(self):
        print("Hi! My name is ", self.name)

person1  = Person()
person1.eating()
person1.sleeping()
person1.setMyName("Minhaz")
person1.sayHello()

person2 = Person()
person2.setMyName("Nadia")
person2.sayHello()

class Person:
    def eating(self):
        print("I'm eating")
    def sleeping(self):
        print("I'm sleeping")
    def doMath(self, a, b):
        print("The output is: ", a+b)

    def setMyName(self, name):
        self.name = name
    def sayHello(self):
        print("Hi! My name is ", self.name)
    def setAge(self, age):
        self.age = age
    def sayAge(self):
        print("My age is: ", self.age)
    def setPerson(self, name, age):
        self.name = name
        self.age = age
    def tellMeAboutYourself(self):
        print("My name is: ", self.name , "\nMy age is: ", self.age)

person1 = Person()
person1.setMyName("Minhaz")
person1.setAge(22)
person1.sayHello()
person1.sayAge()
person1.tellMeAboutYourself()

person1.setPerson("Saimon", 18)
person1.tellMeAboutYourself()