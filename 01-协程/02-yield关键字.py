# -- coding: utf-8 --
# @Time : 2022/8/11 11:20
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 02-yield关键字.py
# @Software: PyCharm

def func1():
    yield 1
    yield from func2()
    yield 2


def func2():
    yield 3
    yield 4


f1 = func1()
print(f1)
for item in f1:
    print(item)


