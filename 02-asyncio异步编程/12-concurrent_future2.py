# -- coding: utf-8 --
# @Time : 2022/8/17 15:44
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 12-concurrent_future2.py
# @Software: PyCharm

import time
import asyncio
import concurrent.futures

def func1():
    # 某个耗时操作
    time.sleep(2)
    return "SB"

async def main():
    loop = asyncio.get_running_loop()
    # 第一步： 内部会先调用 ThreadPoolExecutor的submit方法去线程池申请一个线程去执行 func1函数，并返回一个
    # concurrent.futures.Futures对象。
    # 第二步：调用asyncio.wrap_future将concurrent.futures.Future对象包装为asyncio.Future对象。
    # 因为concurrent.futures.Future对象不支持await语法，所以需要包装为asycio.Future对象才能使用。

    fut = loop.run_in_executor(None, func1)

    result = await fut
    print("default thread pool", result)


asyncio.run(main())
