# Tuple: ordered, immutable, allow duplicate elements

myTuple = (1, 2, 3)
print(myTuple)

print(myTuple[0])

# error
# myTuple[0] = 4

print(len(myTuple))

myList = list(myTuple)
myList.append(4)
print(myList)

