class GhostBus:
    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pick(self, p):
        self.passengers.append(p)


bus1 = GhostBus()
bus1.pick('ky')
print(bus1.__init__.__defaults__)
bus2 = GhostBus(['kiruen'])
print(bus1.__init__.__defaults__, bus2.__init__.__defaults__)
print(bus1.passengers, bus2.passengers)
print(bus1.passengers is bus2.__init__.__defaults__[0])
print(bus2.passengers is bus2.__init__.__defaults__[0])


class Bus:
    def __init__(self, passengers=None):
        if passengers:
            self.passengers = list(passengers)
        else:
            self.passengers = []

    def pick(self, p):
        self.passengers.append(p)


people = [1, 2, 3]
bus1 = Bus(people)
bus2 = Bus(people)
bus2.pick(4)
print(bus1.passengers, bus2.passengers)

import weakref


def bye():
    print('bye~')


s1 = {1, 2, 3}
s2 = s1
f = weakref.finalize(s1, bye)
del s1
print(f.alive)
# del s2
s2 = {1}
print(f.alive)

import weakref

s = {1, 2, 3}
wref = weakref.ref(s)
print(wref())
s = {1, 2}
print(wref())
# input()
print(wref())

a = 1
b = 1
print(a is b)

from collections import namedtuple
from array import array


# vector = namedtuple('Vector', ['x', 'y', 'typecode'])


class Vector2d:
    __slots__ = ('__x', '__y')
    typecode = 'd'

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        # self.__z = x + y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        self.__y = val

    def __hash__(self):
        return hash(self.__x) ^ hash(self.__y)

    def __iter__(self):
        return (self.x, self.y).__iter__()

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + \
               bytes(array(self.typecode, self))

    def __repr__(self):
        return "{}({!r}，{!r})".format(type(self).__name__, *self)

    @classmethod
    def from_bytes(cls, octets):
        type_code = chr(octets[0])
        memv = memoryview(octets[1:]).cast(type_code)
        return cls(*memv)

    @staticmethod
    def foo(val):
        print(val)


# vector.from_bytes = from_bytes

print(eval("Vector2d(1, 2)"))
print(bytes('1asfjisajf', encoding='utf8'))

v = Vector2d(2, 3)
# v.__iter__ = __iter__
# v.__bytes__ = __bytes__
code = bytes(v)
print(Vector2d.from_bytes(code).x)

Vector2d.foo(123)

v.y = 222
print(v.y)
print(hash(v))
print(v)

import reprlib
print(reprlib.repr(list(range(100))))
print(reprlib.repr(array('d', range(10))))

class Vector:
    def __init__(self, components):
        self.__components = components

    def __iter__(self):
        return iter(self.__components)

    def __getitem__(self, item):
        return self.__components[item]

    def __getattr__(self, item):
        cls = type(self)
        return self.__components[(ord(item) - ord('x'))]

vec = Vector(array('i', [1, 2, 3, 4]))
print(vec.y)
print(vec[1:4])

import functools, operator
print(functools.reduce(operator.xor, [1,1,1,1], 0))
print(all(a == b for a, b in zip([1,2,11,4], [1,2,3,4])))
print('<{}>'.format(', '.join(f'{i}' for i in vec)))   # 强类型很头疼


