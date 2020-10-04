import collections.abc as abc
import collections as coll

my_dict = {}
print(isinstance(my_dict, abc.Mapping))


# print(my_dict is abc.Mapping)

class MyHashable:
    def __new__(cls, *args, **kwargs):
        print("hello, it's MyHash")

    def __eq__(self, other):
        return other == self

    def __hash__(self):
        return id(self)


print(hash((1, 2, (3, 4))))

age = my_dict.get('kiruen', 156)
print(age)


def foo():
    '''yes!'''
    print(123)
    return 1


print(foo.__doc__)
# print(map.__doc__)
myhash, _ = MyHashable(), print(MyHashable())
print([callable(o) for o in ([], 1, '23', foo, str)])
print(dir(myhash))
print(foo, foo.__annotations__)


class C: pass


def poo(): pass


print(set(dir(poo)) - set(dir(C)))

import array

print(array.array('h', (i ** 2 for i in range(100))))
print(__name__)


# print(__doc__)
# help(array)

# with open('test.txt', 'w') as f:
#     print(123, file=f)

def foo2(a, b: '第二个参数' = 168, *c, cls=int, **kwargs) -> None:
    print(a, b, c, cls, kwargs)


foo2(1, 2, 3, cls=4, name='ky')

import inspect

sig = inspect.signature(foo2)

for name, param in sig.parameters.items():
    print(param.kind, param.default, param.annotation)
print(sig.return_annotation)

print(foo2.__annotations__)

import operator
from functools import reduce

# print(reduce(operator.mul, range(1, 100)))
print(reduce(operator.concat, [str(x) + ',' for x in range(1, 100)]))

metro_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

my_getter = operator.itemgetter(2, 0)
for city in sorted(metro_data, key=operator.itemgetter(2)):
    print(my_getter(city))

print([name for name in dir(operator) if not name.startswith('_')])
lower = operator.methodcaller('lower')
print(lower('1asfdASAD'))

import functools, unicodedata

mul7 = functools.partial(operator.mul, 7)
print(mul7(21))

nfc = functools.partial(unicodedata.normalize, 'NFC')
s1 = 'café'
s2 = 'cafe\u0301'
print(nfc(s1), nfc(s2))

foo2_plus = functools.partial(foo2, 1, 2, 3, cls=4)
foo2_plus(name='ky')

import time

global_registery = []


def register(func):
    global_registery.append((func, time.localtime()))
    return func


@register
def foo3():
    print('foo3!')


print(global_registery)

import dis

dis.dis('''
a, b, c = 1, 2, 3
def f(a):
    print(a)
    print(b)
    print(c)
    b = 3
    
f(1)
''')