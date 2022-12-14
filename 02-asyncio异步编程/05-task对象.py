# -- coding: utf-8 --
# @Time : 2022/8/15 11:44
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 05-task对象.py
# @Software: PyCharm

'''
白话： 在时间循环中添加多个任务的。

Tasks用于并发调度协程，通过asyncio.create_task(协程对象)的方式创建Task对象，这样可以让协程加入事件循环中等待被调度执行。
除了使用asyncio.create_task()函数以外，还可以用低层级的loop.create_task()或ensure_future()函数。不建议手动实例化Task对象。


'''

import asyncio

async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return '返回值'


async def main():
    print("main开始")

    # 创建协程，将协程封装到一个Task对象中并立即添加到事件循环的任务列表中，等待事件循环去执行(默认是就绪状态)
    task1 = asyncio.create_task(func())

    # 创建协程，将协程封装到一个Task对象中并立即添加到事件循环的任务列表中，等待事件循环去执行(默认是就绪状态)
    task2 = asyncio.create_task(func())

    print("main结束")

    # 当执行某协程遇到IO操作时，会自动切换其它执行任务。
    # 此处的 await是等待相应的协程全部执行完毕并获取结果。
    ret1 = await task1
    ret2 = await task2
    print(ret1)
    print(ret2)

asyncio.run(main())

