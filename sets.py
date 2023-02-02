# Sets: unordered, mutable, not duplicates

myset = {1, 2, 4, 3, 3}
print(myset) # 1, 2, 3, 4


myList = [5, 4, 1, 6, 7, 2, 1]
myset2 = set(myList)
print(myset2)

odd = {1, 3, 5, 7, 9}
even = {2, 4, 6, 8, 10}
prime = {2, 3, 5, 7, 11}

inter = odd.intersection(prime)
uni = odd.union(prime)
diff = odd.difference(prime)

print(inter)
print(uni)
print(diff)
