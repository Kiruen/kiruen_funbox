import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __repr__(self):
        return "Proxy: A List_{}".format(self._cards)

    def __bool__(self):
        return False

    def __call__(self, *args, **kwargs):
        return args[0]

    def __add__(self, other):
        return 1 + other

fd = FrenchDeck()
print(fd[3])
for card in fd:
    print(card)

IDCard = collections.namedtuple("IDCard", ["name", "id"])
mycard = IDCard("kiruen", "321324")
print(mycard)

for i in range(1, 5):
    print(choice(fd))

print(Card("Ka", "hearts") in fd)
print(fd.__len__())


print("{}".format(fd))
print("%s" % fd)
print(1 if fd else 0)
print(fd(23))
print(ord('在'))
print(ord(c) for c in '1234abcd')
print(list((ord(c) for c in '1234abcd')))

import sys
print(sys.version_info)

my_items = [("No.%s" % id, id) for id in range(0, 10)]
for name, _ in my_items:
    print(name, _)

for item in my_items:
    print("%s/%s" % item)

a, *nums, c, d = range(1, 100)
print(nums)

if fd + -1:
    print(125)
if fd:
    print(123)
if fd or mycard:
    print(124)

l = []
l.extend([1,2,3])
print(l)
l.append([1,2,3])
print(l)

print(l[slice(1,2)])

l = list(range(10))
l[1:3] = [6, 6, 6, 6, 6]
print(l)

str1 = "123"
str2 = "456"
print(id(str1))
str1 += str2
print(id(str1))

import dis
s, a, b = [1,3,5], 1, 3
print(dis.dis('s[a] += b'))

l3d = [[[1,2,3,4],[1,2,3,4]],[[1,2,3,4],[1,2,3,4]]]
# print(l3d[1,...])
print(...)

if a == 1 or \
       b == 2:
    print(...)

# from . import test1
# print(test1.srs)

a = [1]
print(a == [1], a is [1])

a = [i for i in range(10)]
print(a[2:-2:-2])
print(a[-2:2:-2])

# import itertools as it
# it.islice()

print({i:[5 - i] * 5 for i in range(5)})
print({('%s' % i) * i for i in range(1, 6)})

print([x for sub1 in l3d for sub2 in sub1 for x in sub2])

mat = [[1,2,3],[1,5,6],[7,8,9]]
print([x for row in mat if sum(row) > 7
            for x in row if x % 3 == 0])

for i, name in enumerate(mat, 1):
    print("%d, %s" % (i, name))

#jfzhai@ustc.edu.cn


print(collections.namedtuple('Student', ['name', 'age', 'score']))
class Student:
    def __init__(self, name):
        self.name = name
        print('stu:%s' % name)

    def __repr__(self):
        return self.name * 2

p = Student('ky')
print(p)

# 输出执行堆栈
import traceback
def f1():
    for line in traceback.format_stack():
        print(line)
def f2():
    f1()
f2()


# 动态强类型（不存在隐式转换）
setattr(p, 'name', 'kiruen')
print(p, getattr(p, 'name'))

print(int.__bases__)

# python.exe -m py_compile test1.py
#import py_compile as pc
#pycodeobject?
#py_compile.compile()
# 而且import module 语句会自动执行编译
import dis
dis.dis("setattr(p, 'name', 'kiruen')")

# project 机器学习 数据分析 推荐论文复现

names = ['ky', 'kiruen']
lengths = [len(n) for n in names]
longest_name = None
longest_len = 0
for name, length in zip(names, lengths):
    if length > longest_len:
        longest_name = name
        longest_len = length

print(longest_name, longest_len)

import itertools
lengths.append(12)
for name, length in itertools.zip_longest(names, lengths):
    if length > longest_len:
        longest_name = name
        longest_len = length

print(longest_name, longest_len)

# for的else块
for i in range(10):
    print(i)
else:
    print(i)


import json
def get_myitem(str, *keys):
    try:
        result_dict = json.loads(str)
    except ValueError as e:
        print("出错了！", e)
    else:
        return tuple(result_dict[key] for key in keys)

print(get_myitem('{"name":"kiruen", "age":1}', "age", "name"))






