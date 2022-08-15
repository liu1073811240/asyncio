# -- coding: utf-8 --
# @Time : 2022/8/15 10:54
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 02-await.py
# @Software: PyCharm

import asyncio

async def func():
    print("来玩呀")
    response = await asyncio.sleep(2)

    print("结束", response)

asyncio.run(func())
