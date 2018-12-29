class Person:
    def eating(self):
        print("I'm Eating")

    def __init__(self):
        self.name = "N/A"
        self.age = 0

    def tell(self):
        print("I am {}, my age is {}".format(self.name,self.age))

    def setPerson(self, name, age):
        self.name = name
        self.age = age

person1 = Person()
person1.tell()
person1.setPerson("Ishita", 21)
person1.tell()


class Person:
    def eating(self):
        print("I'm Eating")

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def tell(self):
        print("I am {}, my age is {}".format(self.name,self.age))

    def setPerson(self, name, age):
        self.name = name
        self.age = age
    def __del__(self):
        print("Destructor Called for ", self.name)

person2 = Person("Azimov", 35)
person2.tell()

person3 = Person("Solaris", 29)
person3.tell()