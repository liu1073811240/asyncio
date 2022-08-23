# -- coding: utf-8 --
# @Time : 2022/8/23 15:50
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 15-异步上下文管理器.py
# @Software: PyCharm

import asyncio


class AsyncContextManager:
    def __init__(self):
        self.conn = conn

    async def do_something(self):
        # 异步操作数据库
        return 666

    async def __aenter(self):
        # 异步链接数据库
        self.conn = await asyncio.sleep(1)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        # 异步关闭数据库连接
        await asyncio.sleep(1)


async def func():
    async with AsyncContextManager() as f:
        result = await f.do_something()
        print(result)

asyncio.run(func())
