# Dict: key-value pairs, unordered, Mutable
myDict = {2 : "b", 1:"a", 3:"c", 4: "d"}
print(myDict)

value = myDict[2]
print(value)

# error
# value = myDict[4]
# print(value)

if 5 in myDict:
    print("exist")
else:
    print("Not Exist")


print(2 in myDict)
myDict.pop(2)
print(2 in myDict)

print(myDict)
test = myDict.popitem()
print(myDict)
print(test) # Tuple (key, value)

for key, value in myDict.items():
    print(key, value)

myDict_cpy = myDict
myDict_cpy[5] = "e"

print(myDict)
print(myDict_cpy)

# copy 
myDict_cpy = dict(myDict)
myDict_cpy = myDict.copy()
