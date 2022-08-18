# -- coding: utf-8 --
# @Time : 2022/8/16 10:36
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 07-task对象3.py
# @Software: PyCharm


import asyncio

async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)

    return '返回值'

task_list = [
    func(),
    func()
]

done, pending = asyncio.run(asyncio.wait(task_list))
print(done)

