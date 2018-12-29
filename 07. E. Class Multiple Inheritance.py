class BasicCalculator:
    def add(self, a,b):
        return a+b
    def sub(self, a ,b):
        return a-b

class LittleAdvanceCalculator(BasicCalculator):
    def mul(self,a,b):
        return a*b

class DivisionCalculator:
    def division(self, a,b):
        if(b == 0):
            return ("Divide by zero isn't possible")
        else:
            return a/b

class FullCalculator(LittleAdvanceCalculator,DivisionCalculator):
    def setName(self, name):
        self.name = name
    def sayName(self):
        print("My Name is ", self.name)

obj1 = FullCalculator()
obj1.setName("Calci")
obj1.sayName()
print("Adding: ",obj1.add(5,10))
print("Subtracting: ",obj1.sub(20,2))
print("Multiplying: ",obj1.mul(10,2))
print("Division: ",obj1.division(15,3))
print("Divide by zero: ",obj1.division(15,0))