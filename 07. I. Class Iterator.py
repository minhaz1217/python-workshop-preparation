myList = [1,2,3]
i = iter(myList)
print(i)
print(i.__next__())
print(next(i))
print(i.__next__())
try:
    print(i.__next__()) #throws an error as the list has finished
except:
    print("No value in the iterator")

print(myList)


class Cows:
    def __init__(self, n):
        self.n = n
        self.i = n
    def __iter__(self):
        return self

    def __next__(self):
        if self.i > 0:
            self.i = self.i-1
            return self.i+1
        else:
            #self.i = self.n #difference with this and without this is that the value needs to reset.
            raise StopIteration

cow1 = Cows(5)
for l in cow1:
    print(l)

for l in cow1: #without the reset this loop won't print anything.
    print(l)

print(list(iter(cow1)))