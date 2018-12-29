class BasicCalculator:
    def add(self, a,b):
        return a+b
    def sub(self, a ,b):
        return a-b

class LittleAdvanceCalculator(BasicCalculator):
    def mul(self,a,b):
        return a*b
    def sub(self,a,b):
        return b-a

obj1 = LittleAdvanceCalculator()
print("Adding: ", obj1.add(15,20))
print("Multiplication: ", obj1.mul(5,2))
print("New Subtraction: ", obj1.sub(5,10))
