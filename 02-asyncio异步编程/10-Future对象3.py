# -- coding: utf-8 --
# @Time : 2022/8/16 11:38
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 10-Future对象3.py
# @Software: PyCharm

import time
from concurrent.futures import Future
from concurrent.futures.thread import ThreadPoolExecutor
from concurrent.futures.process import ProcessPoolExecutor

def func(value):
    time.sleep(1)
    print(value)

pool = ThreadPoolExecutor(max_workers=5)
# pool = ProcessPoolExecutor(max_workers=5)

for i in range(10):
    fut = pool.submit(func, i)
    # print(fut)

