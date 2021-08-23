from collections import namedtuple


if "oh my god!":
    print("it work!")
else:
    print("go back")

fruits = {'orange':1000, 'banana':600, 'apple':800}
print(fruits.get('orange'))

Point = namedtuple('point', 'x y')
p = Point(11, 22)
print(p.__doc__, p)
p = p._replace(x = 100)
print(p)
d = p._asdict()
print(d)
print(d['y'])