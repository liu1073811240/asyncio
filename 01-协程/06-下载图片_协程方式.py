# -- coding: utf-8 --
# @Time : 2022/8/12 9:58
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 06-下载图片_协程方式.py
# @Software: PyCharm

import aiohttp
import asyncio


async def fetch(session, url):
    print("发送请求：", url)
    async with session.get(url, verify_ssl=False) as response:
        content = await response.content.read()

        file_name = url.rsplit('/')[-1]
        with open(file_name, mode='wb') as file_object:
            file_object.write(content)

        print("下载完成", url)


async def main():
    async with aiohttp.ClientSession() as session:
        url_list = ["http://img.netbian.com/file/2022/0810/2210450pka0.jpg",
                    "http://img.netbian.com/file/2022/0720/004410CGAKF.jpg",
                    "http://img.netbian.com/file/2022/0712/234912VQcQL.jpg"]

        tasks = [asyncio.create_task(fetch(session, url)) for url in url_list]

        await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())
