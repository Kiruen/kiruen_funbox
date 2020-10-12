import os, sys, time
import requests

DEST_DIR = '.\\imgs'

def show(data):
    print(data, end='  ')
    sys.stdout.flush()

def save_file(img, filename):
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:
        fp.write(img)

def download(url):
    # print(f'downloading {url}')
    resp = requests.get(url)
    if resp.status_code == 404:
        raise requests.exceptions.HTTPError('404 not found!')
    # print(f'Ok!')
    time.sleep(0.2)
    return resp.content

def download_many(count=5):
    url_base = 'https://www.tupianzj.com/meinv/20200914/{:0>6d}.html'

    for i in range(217448, count + 217448):
        data = download(url_base.format(i))
        save_file(data, f'{i}.html')
        time.sleep(0.2)


def main(download_many, count):
    t0 = time.time()
    download_many(count)
    print('elapsed: {:.2f}s'.format(time.time() - t0))


if __name__ == '__main__':
    main(download_many, 2)