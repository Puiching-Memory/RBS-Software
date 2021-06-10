import re
from fake_useragent import UserAgent
import requests
import pyperclip
import time
import os


def msg_input():  # 这个模块用于下载地址和路径
    print('-' * 106)
    url = input('请输入下载链接，不输入将默认下载粘贴板内的链接：')
    path = input('请输入保存路径，默认为当前文件夹：')
    print('-' * 50, 'data', '-' * 50)
    if url == '':
        url = pyperclip.paste()
    if path == '':
        path = os.getcwd() + '/'

    try:
        filename = url[url.rindex('/') + 1:]
        path = path + url[url.rindex('/') + 1:]
        return url, path, filename
    except Exception as e:
        print('这似乎不是一个有效的链接：', url, '\n', '\n\t\t\t\t\t\t', e)


def check(_str):  # 这个模块用于检测文件是否非法命名导致无法保存
    pattern = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    title = re.sub(pattern, "_", _str)  # 替换为下划线
    exhibition = ('发现非法命名', _str, '已更改为', title)
    return title


def format_float(num):  # 这个模块用于转换浮点数
    return '{:.2f}'.format(num)


def downloader(url, path, filename):
    try:
        start = time.time()
        a_g = UserAgent()
        size = 0
        chunk_size = 1024
        content_tmp = 0
        time1 = time.time()
        response = requests.get(url=url, headers={"User-Agent": a_g.random}, stream=True)
        content_size = int(response.headers['Content-Length'])

        if response.status_code == 200:
            print('[文件名]：%s \n[文件大小]：%0.2f Mb\n[保存路径]：%s\n[目标链接]：%s' % (filename, content_size / chunk_size / 1024, path, url))
            f = open(path, mode='wb')
            for data in response.iter_content(chunk_size=chunk_size):
                if data:
                    f.write(data)
                    size += len(data)
                    if time.time() - time1 > 2:
                        speed = (size - content_tmp) / 1024 / 1024 / 2
                        content_tmp = size
                        print('\r' + "[已经下载]：" + int(size / content_size * 65) * ">" + ' [' + str(
                        round(size / chunk_size / 1024, 2)) + "Mb] " + '[' + str(
                        round(float(size / content_size) * 100, 2)) + "%]" + '[' + format_float(speed) + 'Mb /2s]', end="")
                        time1 = time.time()
            f.close()
        end = time.time()
        print('\n', '-' * 50, 'End', '-' * 50)
        print('\n' + '下载完成！用时%.f分%.2f秒' % ((end-start) / 60, (end-start)))
    except BaseException as e:
        print('下载失败，原因是下载过程中出现了一些错误，以下是捕获到的错误：', '\n\n', e)




if __name__ == '__main__':
    try:
        data = msg_input()
        # print(data)
        check_list = ['/', '\\', ':', '|', '*', '<', '>', '?', '"']
        if any(key in data[2] for key in check_list):
            title = check(data[2])
        downloader(data[0], data[1], data[2])  # 下载地址，保存地址，文件名
    except Exception as e:
        print('\n\t\t\t\t\t\t', e)

