# -- coding: utf-8 --
# @Time : 2022/8/11 11:30
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 03-asyncio编程.py
# @Software: PyCharm

import asyncio

@asyncio.coroutine
def func1():
    print(1)
    yield from asyncio.sleep(2)  # 遇到IO耗时操作，自动化切换到tasks中的其它任务
    print(2)

@asyncio.coroutine
def func2():
    print(3)
    yield from asyncio.sleep(1)  # 遇到IO耗时操作，自动化切换到tasks中的其它任务
    print(4)

tasks = [
    asyncio.ensure_future(func1()),
    asyncio.ensure_future(func2())
]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))



