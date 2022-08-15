# -- coding: utf-8 --
# @Time : 2022/8/11 11:57
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 04-async&await关键字.py
# @Software: PyCharm


import asyncio


async def func1():
    print(1)
    await asyncio.sleep(2)  # 遇到IO耗时操作，自动化切换到tasks中的其它任务
    print(2)


async def func2():
    print(3)
    await asyncio.sleep(1)  # 遇到IO耗时操作，自动化切换到tasks中的其它任务
    print(4)

tasks = [
    asyncio.ensure_future(func1()),
    asyncio.ensure_future(func2())
]

# 去生成或获取一个事件循环
loop = asyncio.get_event_loop()

# 将任务放到 任务列表 中
loop.run_until_complete(asyncio.wait(tasks))
