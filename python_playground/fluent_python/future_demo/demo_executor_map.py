from concurrent import futures
from time import sleep, strftime, time

def show(*args):
    print(strftime('[%H:%M:%S]'), end=' ')
    print(*args)


def loiter(n):
    show(f'{"-" * n} loiter({n}): doing nothing for {n}s...')
    sleep(n)
    show(f'{"-" * n} loiter({n}) done')
    return n ** 2

def main():
    t0 = time()

    excutors = futures.ThreadPoolExecutor(max_workers=3)
    results = excutors.map(loiter, range(10))  # 是个生成器诶！
    show(results)
    for i, res in enumerate(results, 1):
        show(f"No.{i} result: {res}")

    # 18s就把所有结果收集好了，顺序执行的话，要45s+
    print("{:.2f} elapsed.".format(time() - t0))

from tqdm import tqdm

if __name__ == '__main__':
    # t0 = time()
    # main()
    # print("{:.2f} elapsed.".format(time() - t0))
    for i in tqdm(range(1024)):
        sleep(.21)

