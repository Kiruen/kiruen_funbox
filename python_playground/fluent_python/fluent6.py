# 开始学习协程！

import inspect


def create_coro1(a):
    print('start!')
    b = yield a  # 返回a并暂停
    print('receive b:', b)
    c = yield a + b  # 返回a + b并暂停
    print('receive c:', c)


coro1 = create_coro1(6)
print(inspect.getgeneratorstate(coro1))
a = next(coro1)  # 还会产出a给你
print('接收到产出值a：', a)
print(inspect.getgeneratorstate(coro1))
aplusb = coro1.send(7)
print('接收到产出值a + b：', aplusb)
print(inspect.getgeneratorstate(coro1))
try:
    coro1.send(28)  # 这里会抛出个异常。。搞不懂python为什么以这种方式把协程停下来
except:
    print(inspect.getgeneratorstate(coro1))


# 预激协程
from functools import wraps

def coroutine(gen_func):
    @wraps(gen_func)  # wraps仅仅就是复制了原函数的一些属性，不想身份被戳穿罢了
    def pre_init(*args, **kwargs):
        gen = gen_func(*args, **kwargs)
        next(gen)  # 预激！
        return gen
    return pre_init

@coroutine
def foo(a, b=10, **kwargs):
    print('已激活!')
    yield a
    yield a ** b
    yield kwargs

gen = foo(10, c=13)
print(inspect.getgeneratorstate(gen))
print(foo.__name__)  # wraps的功劳
for i in gen:
    print(i)



def demo_exit():
    while True:
        try:
            a = yield
        except Exception:
            print('I have stopped')
        else:
            print(f'Got {a}. Go on')

gen = demo_exit()
next(gen)
gen.send(12)
gen.send(12)
gen.send(12)