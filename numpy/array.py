# -*- coding: utf-8 -*-
# @Time    : 2021/2/19 14:14
# @Author  : Han-xun Yu
# @Email   : yuhanxun@126.com
# @File    : ndarray
# @Software: PyCharm

"""

"""
import numpy as np


def init_array():
    print("-----------init_array-----------")

    # 基于py数组创建
    arr = np.array([1, 2, 3])  # 1维
    print_arr(arr)
    print()

    arr = np.array([[1, 2], [3, 4]])  # 2维
    print_arr(arr)
    print()

    arr = np.array([1, 2, 3, 4, 5], ndmin=2)  # 最小维度
    print_arr(arr)
    print()

    shape = [3, 2]

    # 随机值创建
    print("np.empty")
    arr = np.empty(shape, dtype=int)
    print_arr(arr)
    print()

    # 0值创建
    print("np.zeros")
    arr = np.zeros(shape, dtype=int)
    print_arr(arr)
    print()

    """
     order C 和 Fortran 的区别
     比如二维数组 a[2][2]，使用 C，其在内存中存储为
     a[0][0] a[0][1] a[1][0] a[1][1]
     而在 Fortran 里，其顺序为
     a[0][0] a[1][0] a[0][1] a[1][1]
    """
    # 1值创建
    print("np.ones")
    arr = np.ones(shape, dtype=int, order='C')  # order 'C'行优先 'F'列优先
    print_arr(arr)
    print()

    # 等差数列创建
    print("np.arange")
    arr = np.arange(shape[0] * shape[1]).reshape(shape, order='C')
    print_arr(arr)
    arr = np.arange(shape[0] * shape[1]).reshape(shape, order='F')
    print_arr(arr)
    print()

    # 复制数组
    print("np.asarray")
    arr2 = np.asarray(arr)
    print_arr(arr2)
    print()

    return


def operate_array():
    print("-----------operate_array-----------")
    shape = [3, 2]
    arr = np.arange(shape[0] * shape[1])
    print_arr(arr)

    # 形变 -1表示列数不指定，根据指定的行数1来计算列数
    print("np.reshape(2,-1)")
    arr = arr.reshape(2, -1)
    print_arr(arr)  # 指定形状与 原元素数量不匹配将抛出ValueError
    print()

    # 平均 所有元素
    print("np.mean(arr)")
    mean = np.mean(arr)
    print(arr)
    print("mean =>", mean)
    print()

    # 平均 同列平均
    print("np.mean(arr, axis=0)")
    mean = np.mean(arr, axis=0)
    print(arr)
    print("mean =>", mean)
    print()

    # 平均 同行平均
    print("np.mean(arr, axis=1)")
    mean = np.mean(arr, axis=1)
    print(arr)
    print("mean =>", mean)
    print()

    # 转置
    arr = np.array([[1, 2, 3]])
    print(arr.T)
    print(arr.transpose())
    print()

    # 组合2个数组
    a_arr = np.array([1, 2, 3])
    b_arr = np.array([4, 5, 6])
    print(np.concatenate((a_arr, b_arr), axis=0))  # axis=0 ,axis为在哪个维度上进行拼接
    
    a_arr = np.array([[1, 2], [3, 4]])
    b_arr = np.array([[5, 6]])
    print(np.concatenate((a_arr, b_arr.T), axis=1))  

    return


def read_array():
    print("-----------read_array-----------")

    # 取指定index
    arr: np.ndarray = np.arange(10)
    print(arr)
    index_arr = arr[[1, 2, 5]]
    print(index_arr)
    print()

    arr: np.ndarray = np.arange(2 * 3).reshape(2, 3)
    print_arr(arr)
    print()

    # 遍历 flat迭代器
    print("ndarray.flat")
    for element in arr.flat:
        print(element, end=',')
    print()
    print()

    # 拷贝 平铺化 flatten
    print("ndarray.flatten")
    print(arr)
    print("arr.flatten() =>", arr.flatten())
    print("arr.flatten(order='F') =>", arr.flatten(order='F'))
    print()

    # 平铺化 ravel 
    print("ndarray.ravel")
    print(arr)
    ravel_arr = arr.ravel()
    print("arr.ravel()=>", ravel_arr)
    print("修改ravel结果 将影响原数组")
    ravel_arr[0] = 10  # 修改将影响原数组
    print(ravel_arr)
    print(arr)
    print()

    return


def print_arr(arr: np.ndarray):
    # print(arr, "dtype:", arr.dtype, type(arr))
    print(arr)


if __name__ == '__main__':
    # init_array()
    operate_array()
    # read_array()
