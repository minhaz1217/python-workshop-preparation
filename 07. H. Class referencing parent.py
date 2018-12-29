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

class TalkingCalculator(LittleAdvanceCalculator):
    def talkAndAdd(self,a,b):
        print("{} + {} = {}".format(a,b, super(TalkingCalculator, self).add(a,b)))
    def talkAndSub(self, a,b):
        print("Sub1 {} - {} = {}".format(a,b, super(TalkingCalculator, self).sub(a,b)))
    def talkAndSub2(self, a,b):
        print("Sub2 {} - {} = {}".format(a,b, super(LittleAdvanceCalculator, self).sub(a,b)))

obj2 = TalkingCalculator()
obj2.talkAndAdd(1,4)
obj2.talkAndSub(1,4)
obj2.talkAndSub2(1,4)