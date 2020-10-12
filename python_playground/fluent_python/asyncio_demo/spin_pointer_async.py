'旋转指针模块'
__author__ = 'Kiruen'

import sys, threading, time, itertools
import asyncio


class signal:
    '简单的线程通信信号'
    go_on = True

@asyncio.coroutine
def spin(n: int):
    "指针旋转控制函数"
    write, flush = sys.stdout.write, sys.stdout.flush
    pointers = '-\\|/-\\|/'
    for ch in itertools.cycle(pointers):
        write(ch)
        flush()
        try:
            yield from asyncio.sleep(.5)
        except asyncio.CancelledError:
            break
        else:
            write('\x08' * len(ch))


@asyncio.coroutine
def slow_function(n):
    # 假装等待I/O一段时间，结束后会立刻切换回supervisor，然后cancel掉spiner
    yield from asyncio.sleep(n)
    return 42


@asyncio.coroutine
def supervisor():
    """文档字符串：监视器函数"""
    loop = asyncio.get_event_loop()
    spiner = loop.create_task(spin(2))
    # spiner.add_done_callback(lambda x: print('完成！'))
    res = yield from slow_function(2)
    spiner.cancel()
    return res


def main():
    loop = asyncio.get_event_loop()
    res = loop.run_until_complete(supervisor())
    loop.close()
    print(res)

# @asyncio.coroutine
async def foo():
    await asyncio.sleep(.5)
    print(12345)

if __name__ == '__main__':
    # main()
    coro = foo()
    print(coro)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(coro)
    loop.close()
else:
    import functools

    def foo(a, b):
        return a ** b

    _pow2 = functools.partial(foo, 2)
    print(_pow2(20))