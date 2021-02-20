# -*- coding: utf-8 -*-
# @Time    : 2021/2/20 13:34
# @Author  : Han-xun Yu
# @Email   : yuhanxun@126.com
# @File    : math
# @Software: PyCharm

"""

"""

import numpy as np


def random():
    print("--------random---------")

    """
    np.random.rand(d0,d1,...,dn)  d0,d1..dn 表示形状
    返回n维的随机数矩阵。注意，是矩阵， randn为正态分布
    """
    print("np.random.rand(2, 3) =>\n", np.random.rand(2, 3))
    print()

    """
    np.random.random(size)
    返回指定size的[0,1)随机数矩阵，random_sample、ranf、sample和它一样
    """
    print("np.random.random(2, 3) =>\n", np.random.random([2, 3]))
    print()
    """
    np.random.randint(low[,high,size,dtype])
    返回low<=n<high范围的整数，random_integers为dtype=np.int类型
    """
    print("np.random.randint(1, 10) =>", np.random.randint(1, 10))
    print()


def calculate():
    print("--------calculate---------")
    arr = np.array([[1, 2], [3, 4]])

    # 平均值
    print("mean axis=0 =>", np.mean(arr, axis=0))  # axis表示维数 第几维对应位置数相加 
    print("mean axis=0 =>", np.mean(arr, axis=1))

    return


if __name__ == '__main__':
    # random()
    calculate()
