class Farm:
    cows = 0
    fishes = 0
    def __init__(self, cow=0, fish=0):
        self.cows = cow
        self.fishes = fish

    def details(self):
        print("Cows: {} Fishes: {}".format(self.cows, self.fishes))
    def __eq__(self, other): # == operator
        if(self.cows == other.cows and self.fishes == other.fishes):
            return True
        else:
            return False


    def __lt__(self, other): # < operator
        if(self.cows < other.cows):
            return True
        else:
            return False
    def __gt__(self, other): # > operator
        if(self.cows > other.cows):
            return True
        else:
            return False
    def __ge__(self, other): # >= operator
        if(self.cows >= other.cows):
            return True
        else:
            return False
    def __le__(self, other): # <= operator
        if(self.cows <= other.cows):
            return True
        else:
            return False
    def __len__(self):
        return self.cows + self.fishes
    def __add__(self, other):
        if(type(self) == type(Farm()) and type(other) == type(Farm()) ):
            x = other.cows + self.cows
            y = other.fishes + self.fishes
            return Farm(x,y)
        else:
            x = self.cows + other
            y = self.fishes + other
            return Farm(x,y)
    #
    # def __radd__(self, other):
    #     self.cows = other
    #     self.fishes = other
    #     return Farm(self.cows , self.fishes)

TokisFarm = Farm(2,3)
JannatsFarm = Farm(2,4)
if(TokisFarm == JannatsFarm):
    print("They are equal")
else:
    print("They are not equal")

print("Toki's Farm: ", len(TokisFarm))

megaFarm = Farm()
megaFarm =megaFarm+ 5
#megaFarm =5+ megaFarm #this throws an error without the __radd magic method

megaFarm.details()
megaFarm = TokisFarm + JannatsFarm
megaFarm.details()

print(dir(Farm()))
