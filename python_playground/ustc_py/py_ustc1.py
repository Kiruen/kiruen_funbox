x = 1
print(id(x))
x += 1
print(id(x))

print(1_000_000)
print(0xff_ea_cc_0f)
print(1.02e-2)

print([1, 2] + [3, 4])
print((1, 2) + (3, 4))

s1, s2 = {1, 2, 3, 4}, set('3456')  # 别忘了字符串也是序列
print({} == dict())
print(s2)
s2 = {int(x) for x in s2}
print(s1 - s2)

import collections

myclass = collections.namedtuple('MyClass', ('age', 'name'))
d1 = {
    myclass(1, 'kir'): 1,
}
print(d1)

my_dict = dict([('kiruen', 1), (11, 'kiruen')])
print(my_dict)

import sys
with open('test', 'a+') as fp:
    sys.stdout = fp
    sys.stderr = fp
    sys.stdout.write("asfafffs")
    sys.stdout.flush()
    # raise Exception('sadshdu')
    sys.stdin = fp
    print(input("输入值为"))