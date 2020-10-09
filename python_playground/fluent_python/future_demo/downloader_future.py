from concurrent import futures
# from .downloader_base import download, main
# import sys
# sys.path.append("..")
from future_demo.downloader_base import download, main
from functools import singledispatch


# @download_many.register(int)
def _(count):
    workers_count = count
    url_base = 'https://www.tupianzj.com/meinv/20200914/{:0>6d}.html'
    id_base = 217448
    with futures.ThreadPoolExecutor(workers_count) as executor:
        res = executor.map(download, (url_base.format(id_base + i) for i in range(count)))


# @singledispatch
def download_many(count):
    workers_count = min(3, count)  # 区分任务数 and 线程数
    url_base = 'https://www.tupianzj.com/meinv/20200914/{:0>6d}.html'
    id_base = 217448
    future_list = []
    with futures.ThreadPoolExecutor(workers_count) as executor:
        for i in range(count):
            url = url_base.format(id_base + i)
            future = executor.submit(download, url)
            print("任务：{!r} url：{}".format(future, url))
            future_list.append(future)

        for future in futures.as_completed(future_list):
            print("任务：{!r} 返回的结果：{}".format(future, future.result()))


if __name__ == '__main__':
    # main(download_many, 5)
    main(download_many, 5)
