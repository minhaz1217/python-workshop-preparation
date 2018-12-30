a = 5
b = 6
str = "I got {} and {} in my exam.".format(a,b)
print(str)
print("%s" %str)
print("%.5s" %str)

dhk = "Dhaka"
bsl = "Barisal"
syl = "sylhet"
route = " -> ".join([dhk, bsl, syl]) #notice that we had to put them inside brackets
print(route)

print("Upper case: ", dhk.upper())
print("Lower case: ", dhk.lower())
print("Case fold: ", dhk.casefold()) #case fold is mainly used to compare cases in other languages.
print("Capitalize case: ", syl.capitalize())
print("Swap case: ", dhk.swapcase())
