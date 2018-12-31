setA = {1,2,3,4,5,6,7,8}
setB = {1,2,3,9,10}
print("setA: ", setA)
print("setB: ", setB)
print("A U B = ", setA.union(setB))
print("A intesection B = ", setA.intersection(setB))
print("A-B = ",setA.difference(setB))
print("B-A = ",setB.difference(setA))

print("A and B disjoint: ",setA.isdisjoint(setB))
setC = {11,12,13}
print("C = ", setC)
print("A and C disjoint: ", setA.isdisjoint(setC))
setD = {1,2,3}

print("D = ", setD)
print("A is a subset of D: ", setA.issubset(setD))
print("D is a subset of A: ", setD.issubset(setA))
print("A is a superset of D: ", setA.issuperset(setD))
print("D is a superset of A: ", setD.issuperset(setA))

