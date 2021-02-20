# -*- coding: utf-8 -*-
# @Time    : 2021/2/19 17:04
# @Author  : Han-xun Yu
# @Email   : yuhanxun@126.com
# @File    : matrix
# @Software: PyCharm

"""

"""
import numpy as np


def init_matrix():
    print("----------init_matrix----------")

    # 基于py数组创建
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    A = np.mat(data, int)
    print(A)

    # 基于np数组创建
    data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    A = np.mat(data, int)
    print(A)

    return


def read_matrix():
    print("----------read_matrix----------")

    data = [[17, 21, 2],
            [17, 18, 2],
            [5, 21, 19]]
    A = np.mat(data, int)

    # 遍历矩阵
    for x in np.nditer(A):
        print(x, end=",")
    print()
    print()

    # 输出矩阵 （分数） 下面用逆矩阵做测试
    import fractions
    keyMatrixInverse = np.linalg.inv(data)
    np.set_printoptions(formatter={'all': lambda x: str(fractions.Fraction(x).limit_denominator())})
    print(keyMatrixInverse)
    return


def operate_matrix():
    print("----------operate_matrix----------")

    a = np.arange(2 * 3).reshape(2, 3)
    b = np.arange(3 * 2).reshape(3, 2)
    c = np.arange(2 * 2).reshape(2, 2)
    d = np.arange(start=4 * 4, stop=4 * 4 + 4).reshape(2, 2)

    # 转数组
    print(a.tolist())

    # 对应位置元素相乘
    print("np.multiply")
    print("mxn矩阵  2矩阵必须m1=m2 n1=n2")
    print(np.multiply(c, d))  # 简写 c*d
    # print(np.multiply(a, b)) # 行列不匹配，相乘将抛出ValueError
    print()

    # 乘法 单矩阵
    print("np.dot")
    print("mxn矩阵  2矩阵必须n1=m2")
    print(np.dot(a, b))
    print(np.dot(b, c))
    # print(np.dot(a, c)) # 行列不匹配，相乘将抛出ValueError
    print()

    # 乘法 多矩阵
    print("------------np.matmul-------------")
    a = np.arange(2 * 2 * 4).reshape((2, 2, 4))
    b = np.arange(2 * 2 * 4).reshape((2, 4, 2))
    c = np.arange(1 * 2 * 4).reshape((1, 4, 2))

    print("a", a)
    print("b", b)
    print("c", c)

    """
    当np.matmul(a, b)时，
    1.会把a看成2个2x4的矩阵a1和a2，
    2.同样b看成2个4x2的矩阵b1和b2, 
    3.然后做np.dot(a1, b1), np.dot(a2, b2), 结果合并为一个shape为2 * 2 * 2的矩阵
    """
    print("np.matmul(a, b) =>")
    print(np.matmul(a, b))
    print()

    """
    当np.matmul(a, c)
    时，会把a看成2个2x4的矩阵a1和a2，c看成1个4x2的矩阵
    c1
    // 这里会广播c1，然后做np.dot(a1, c1)
    np.dot(a2, c1) <= 注意：都是c1
    // 结果合并为一个shape为2 * 2 * 2
    的矩阵
    """
    print("np.matmul(a, c) =>")
    print(np.matmul(a, c))  # np.matmul(a, c) 简写 a@c
    print()

    return


if __name__ == '__main__':
    init_matrix()
    read_matrix()
    operate_matrix()
