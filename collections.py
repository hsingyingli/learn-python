# collections: Counter, namedtuple, OrderedDict, defaultdict, deque

from collections import Counter


a = "aabbccddeeeeqweqweq"

myCounter = Counter(a)
print(myCounter)
print(myCounter.most_common(2)) # List of tuple [('e', 6), ('q', 3)]



from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

pt = Point(1, -1)
print(pt)


# python3.7 dict is ordered
from collections import OrderedDict 

order_dict = OrderedDict()

order_dict['b'] = 2
order_dict['a'] = 1
order_dict['c'] = 3
order_dict['d'] = 4
order_dict['e'] = 5
order_dict['f'] = 6
print(order_dict)


from collections import defaultdict

d = defaultdict(int)
d['a'] = 1
d['b'] = 2

print(d['a']) # 1
print(d['c']) # default : 0


from collections import deque

d = deque()

d.append(1)
d.append(2)
d.append(3)
d.append(4)

print(d)

d.appendleft(0)
print(d)

d.pop()
print(d)
d.popleft()
print(d)
d.clear()
print(d)

d.extend([4, 1, 2, 3])
print(d)
