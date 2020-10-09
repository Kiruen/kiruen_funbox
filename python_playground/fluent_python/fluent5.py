from fractions import Fraction


def gen123():
    yield 1
    yield 2
    yield 3


for i in gen123():
    print(i)

import re

pattern = re.compile('\w{2,}')
print(list(pattern.finditer("12 as ddsa d a ss")))


# print(NotImplemented)


def foo(arg):
    print(arg)


foo(i for i in range(10))

print(Fraction(1, 3))

import itertools

gen = itertools.count(1, Fraction(1, 3))
for i in range(10):
    print(next(gen))

gen1 = gen = itertools.count(1, .2)  # 0.25
gen1 = itertools.takewhile(lambda n: n < 3, gen1)
print(list(gen1))

print(list(itertools.islice(range(0, 101), 51, None, 10)))
print(list(itertools.compress('Kiruen', (1, 0, 0, 1, 1, 1))))  # str(


def print_all(*iters):
    for it in iters:
        yield from it


print(list(print_all(range(1, 10), range(10, 0, -1))))
# print(b'0' + bytes('adas', encoding='utf8'))
# print(bytes('adas\0', encoding='utf8'))
gen = (b for b in bytes('adas\0', encoding='utf8'))
print(all(gen))
# print(next(gen))

gen = (n for n in [0, 2, 4])  # [0, 2, 4]
print(all(gen))
print(next(gen))
gen = (n for n in [0, 2, 4])
print(any(gen))
print(next(gen))

print(sum([1, 2, 3, 4], 100))

# 抽炸弹
# import numpy as np
import random


def f():
    return random.randint(20, 30)


bomb = iter(f, 25)
for i, card in enumerate(bomb, 1):
    print(card)
else:
    print(f"抽了{i + 1}次")


with open("test.txt", 'r', encoding='utf8') as fp:
    for i, line in enumerate(iter(fp.readline, "#over\n"), 1):
        line1 = line.replace('\n', '')
        print(f"第{i}行：", line1 if line1 is not '' else '<空行>')

print(fp)
print(line1) # 额，局部变量还留着哪


num = 0
for i in range(10):
    for j in range(20):
        num += j
    # continue
    break
else:
    print("最终的i是：", i)  # 不会执行


# 使用上下文管理器实现放大镜
class BiggerMirror:
    def __enter__(self):
        import sys
        self.original_write = sys.stdout.write
        sys.stdout.write = self.bigger_write
        return "BiggerMirror is on!"

    def bigger_write(self, content):
        self.original_write(str.upper(content))

    def __exit__(self, exc_type, exc_val, exc_tb):
        import sys
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print('Please DO NOT divide by zero!')
            return True

with BiggerMirror() as bm:
    print('hi, i am kiruen')

print(bm)

import contextlib as cl
# 生成器代码是真的短小精悍
def foo():
    print('start!')
    yield 'initial value'
    print('doing something~')
    yield None
    print('end!')
    yield None  # 这个为什么不能丢？next要执行到yield为止啊

gen = foo()
# 模拟初始化
next(gen)
# 执行某些逻辑
print(next(gen))
# 模拟finally
next(gen)

@cl.contextmanager
def looking_smaller():
    import sys
    orig = sys.stdout.write
    def smaller_write(text):
        orig(str.lower(text))
    sys.stdout.write = smaller_write
    try:
        yield '缩小镜开启！'
    except ZeroDivisionError:
        msg = '除数不能是0！'
    finally:
        sys.stdout.write = orig
        if msg:
            print(msg)

gen = looking_smaller()
with gen as mirror:
    print("HAFUIHFUAS")
    print(mirror + (1 / 0))

