# -- coding: utf-8 --
# @Time : 2022/8/11 11:09
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 01-greenlet.py
# @Software: PyCharm


from greenlet import greenlet

def func1():
    print(1)
    gr2.switch()
    print(2)
    gr2.switch()

def func2():
    print(3)
    gr1.switch()
    print(4)


gr1 = greenlet(func1)
gr2 = greenlet(func2)

gr1.switch()