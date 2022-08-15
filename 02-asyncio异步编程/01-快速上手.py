# -- coding: utf-8 --
# @Time : 2022/8/15 9:42
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 01-快速上手.py
# @Software: PyCharm

import asyncio

async def func():

    print("快来了")

result = func()

# loop = asyncio.get_event_loop()
# loop.run_until_complete(result)

# asyncio.run(result)  # py3.7以后才能使用，等同于上述两句代码

