# -- coding: utf-8 --
# @Time : 2022/8/23 15:23
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 14-异步迭代器.py
# @Software: PyCharm

import asyncio


class Reader(object):
    """ 自定义异步迭代器（同时也是异步可迭代对象）"""

    def __init__(self):
        self.count = 0

    async def readline(self):
        # await asyncio.sleep(1)
        self.count += 1
        if self.count == 100:
            return None

        return self.count

    def __aiter__(self):
        return self

    async def __anext__(self):
        val = await self.readline()
        if val == None:
            raise StopAsyncIteration

        return val


async def func():
    obj = Reader()
    async for item in obj:
        print(item)


asyncio.run(func())

