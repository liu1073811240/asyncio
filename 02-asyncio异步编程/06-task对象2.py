# -- coding: utf-8 --
# @Time : 2022/8/16 10:14
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 06-task对象2.py
# @Software: PyCharm

import asyncio

async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return '返回值'


async def main():
    print("main开始")

    # 创建协程，将协程封装到一个Task对象中并立即添加到事件循环的任务列表中，等待事件循环去执行(默认是就绪状态)
    # task1 = asyncio.create_task(func())
    # 创建协程，将协程封装到一个Task对象中并立即添加到事件循环的任务列表中，等待事件循环去执行(默认是就绪状态)
    # task2 = asyncio.create_task(func())

    task_list = [
        asyncio.create_task(func(), ),
        asyncio.create_task(func(), )
    ]

    print("main结束")

    # 当执行某协程遇到IO操作时，会自动切换其它执行任务。
    # 此处的 await是等待相应的协程全部执行完毕并获取结果。
    # ret1 = await task1
    # ret2 = await task2
    # print(ret1)
    # print(ret2)
    done, pending = await asyncio.wait(task_list, timeout=None)  # None为等待所有任务完成。
    print(done)
    print(pending)

asyncio.run(main())

