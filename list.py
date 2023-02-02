# Lists: ordered, mutable, allow duplicate element
# simple list
myList = ["apple", "banana", "cherry"]
print(myList)

# allow different type 
myList2 = [1, "2", 3]
print(myList2)

# error
# print(myList2[3])

myList2.append(4)
print(myList2)
myList2.remove("2")
print(myList2)

# error
# myList2.remove("2")
# print(myList2)

myList2.clear()
print(myList2)

# reverse
myList2 = [4, 5, 1, 3, 2]
myList2.reverse()
print(myList2)
myList2.sort()
print(myList2)


# slice 
# list[start:end:gap]
myList3 = [i for i in range(10)]
print(myList3[1: 4: 2])
print(myList3[::-1]) # reverse

# copy a list 
t = myList3.copy()
t = list(myList3)
t = myList3[:]


