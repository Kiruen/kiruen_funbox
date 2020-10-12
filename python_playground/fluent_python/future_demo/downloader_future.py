from concurrent import futures
# from .downloader_base import download, main
# import sys
# sys.path.append("..")
from future_demo.downloader_base import download, main
from functools import singledispatch
from tqdm import tqdm
import requests
import collections as coll

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
    #     with futures.ProcessPoolExecutor(workers_count) as executor:
    with futures.ThreadPoolExecutor(workers_count) as executor:
        for i in range(count):
            url = url_base.format(id_base + i)
            future = executor.submit(download, url)
            print("任务：{!r} url：{}".format(future, url))
            future_list.append(future)
            print("任务：{!r} 返回的结果：{}".format(future, future.result()))


def download_many_advanced(count):
    counter = coll.Counter()
    workers_count = min(3, count)  # 区分任务数 and 线程数
    url_base = 'https://www.tupianzj.com/meinv/20200914/{:0>6d}.html'
    id_base = 217448
    future_list = []
    #     with futures.ProcessPoolExecutor(workers_count) as executor:
    with futures.ThreadPoolExecutor(workers_count) as executor:
        for i in range(count):
            url = url_base.format(id_base + i)
            future = executor.submit(download, url)
            # print("任务：{!r} url：{}".format(future, url))
            future_list.append(future)
            # print("任务：{!r} 返回的结果：{}".format(future, future.result()))

    done_iter = tqdm(futures.as_completed(future_list), total=len(future_list))
    for future in done_iter:
        try:
            res = future.result()
        except requests.exceptions.HTTPError as e:
            err_msg = str(e)
            pass  # print(e)
        else:
            err_msg = ''
            # print(res)

        if err_msg:
            counter['fail'] += 1
        else:
            counter['ok'] += 1
    return counter


if __name__ == '__main__':
    # main(download_many, 5)
    print(download_many_advanced(18))
