# -*- coding: utf-8 -*-
# @Time    : 2021/2/18 15:18
# @Author  : Han-xun Yu
# @Email   : yuhanxun@126.com
# @File    : lang
# @Software: PyCharm

"""
函数定义
循环
"""


def demo_fun(name: str, age: 'int < 0' = 20) -> str:  # ->str 表示该函数的返回值是str类型的
    """
    函数
    :param name: 
    :param age: 
    :return: 
    """
    print("-----------demo_fun----------")
    print(name, type(name))
    print(age, type(age))
    return "hello world"


def loop():
    print("-----------loop----------")
    # 遍历字符串
    print("loop string")
    for letter in 'Python':  # 第一个实例
        print('当前字母 :', letter)
    print()

    # 遍历List
    print("loop array")
    fruits = ['banana', 'apple', 'mango']
    # 直接拿元素
    for fruit in fruits:  # 第二个实例
        print(fruit)
    print()

    # 用index
    print("loop array <- index")
    for index in range(len(fruits)):
        print('index:%d %s' % (index, fruits[index]))
        print()

    # enumerate
    print("loop array <- enumerate")
    for index, e in enumerate(fruits):
        print('index:%d %s' % (index, e))

    return


def if_else():
    print("-----------if_else----------")
    a = 30

    if a > 10 and a < 40:
        print("a>10 and a<40")

    if 10 < a < 40:
        print("10 < a < 40")

    if 10 < a or a > 20:
        print("10 < a or a> 20")

    if a != 10:
        print("a != 10")

    if a < 10:
        print("a < 10")
    elif a < 20:
        print("a < 20")
    else:
        print("a >= 20")

    # 三目运算符 [ <真值> if <条件> else <假值> ] 
    print(True if a > 40 else False)
    return


if __name__ == '__main__':
    # demo_fun("yhx", 1)
    loop()
    if_else()
