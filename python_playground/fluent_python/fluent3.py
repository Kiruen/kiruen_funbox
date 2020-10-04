import functools
import time

def make_avg():
    history = []

    def add_value(value):
        history.append(value)
        total = sum(history)
        return total / len(history)

    return add_value


avg = make_avg()
print(avg(10), avg(11), avg(12))
print(avg.__code__.co_freevars, avg.__code__.co_varnames)
print(avg.__closure__[0].cell_contents)


def make_avg2():
    total = 0
    count = 0

    def add_value(value):
        nonlocal total, count
        total += value
        count += 1
        return total / count

    return add_value


def timer(func):
    def clock(*args):
        t0 = time.perf_counter()
        res = func(*args)
        span = time.perf_counter() - t0
        print("%s finished. Result: %s. Timespan: %s sec" % (func.__name__, res, span))
        return res

    return clock


@timer
def foo(content):
    for i in range(1):
        print(content)


foo(123)
print(foo.__name__)


@functools.lru_cache(maxsize=65536)
@timer
def fab(n):
    if n < 2:
        return 1
    return fab(n - 1) + fab(n - 2)


fab(200)

from functools import singledispatch, singledispatchmethod
from collections import abc


class Parser:
    @singledispatchmethod
    def parse(self, obj):
        return repr(obj)

    @parse.register(str)
    def _(self, str):
        return '<%s>' % str

    @parse.register(tuple)
    @parse.register(abc.MutableSequence)
    def _(self, _seq):
        return [self.parse(o) for o in _seq]

    @parse.register(abc.MutableMapping)
    def _(self, _map):
        return {key: self.parse(value) for key, value in _map.items()}


parser = Parser();
print(parser.parse([1, '123', {'name': ['kiruen', ('ky', 'zheng')]}]))


def remove_element(seq, val):
    i_dead = 0
    is_seq = False
    for i, ele in enumerate(seq):
        if val != ele:
            seq[i_dead] = ele
            i_dead += 1
    remain_count = len(seq) - i_dead
    while remain_count > 0:
        del seq[-1]
        remain_count -= 1


l = [2, 1, 2, 3, 3, 2, 1, 2, 2]
remove_element(l, 2)
print(l)


DEFAULT_FORMATE = 'name：{name}; time：{span:0.8f}s → {res}'

def clock(fmt=DEFAULT_FORMATE):
    def decorate(fun):
        def clocked(*args):
            t0 = time.time()
            res = fun(*args)
            span = time.time() - t0
            name = fun.__name__
            print(fmt.format(**locals()))
            return res
        return clocked
    return decorate

import operator as op

@clock('name：{name}; time：{span:0.8f}s return {res}')
def foo(content):
    s = 0
    for i in range(1000000):
        s += functools.reduce(op.mul, range(1, 20))
    return s

foo(234)