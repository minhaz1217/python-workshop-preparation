
class BasicCalculator:
    def add(self, a,b):
        return a+b
    def sub(self, a ,b):
        return a-b


obj1 = BasicCalculator()

print("Adding: ",obj1.add(5,10))
print("Subtracting: ", obj1.sub(10,5))

class FullCalculator(BasicCalculator):
    def mul(self,a,b):
        return a*b

obj2 = FullCalculator()
print("Adding 2: ", obj2.add(50,10))
print("Subtracting 2: ", obj2.sub(20,15))
print("Multiplying: ", obj2.mul(5,6))




