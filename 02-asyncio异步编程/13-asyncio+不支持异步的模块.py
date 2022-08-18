# -- coding: utf-8 --
# @Time : 2022/8/18 15:36
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 13-asyncio+不支持异步的模块.py
# @Software: PyCharm

import requests
import asyncio


async def download_image(url):
    # 发送网络请求，下载图片(遇到网络下载图片的IO请求，自动化切换其它任务)
    print("开始下载：", url)

    loop = asyncio.get_event_loop()

    # requests模块不支持异步操作，所以就使用线程池来配合实现
    future = loop.run_in_executor(None, requests.get, url)

    response = await future
    print('下载完成')

    file_name = url.rsplit('/')[-1]
    with open(file_name, mode='wb') as file_object:
        file_object.write(response.content)


if __name__ == '__main__':
    url_list = ["http://img.netbian.com/file/2022/0810/2210450pka0.jpg",
               "http://img.netbian.com/file/2022/0720/004410CGAKF.jpg",
               "http://img.netbian.com/file/2022/0712/234912VQcQL.jpg"]

    tasks = [download_image(url) for url in url_list]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))


