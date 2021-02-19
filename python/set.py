# -*- coding: utf-8 -*-
# @Time    : 2021/2/18 16:47
# @Author  : Han-xun Yu
# @Email   : yuhanxun@126.com
# @File    : set
# @Software: PyCharm

"""

"""


def array():
    print("-------array-------")

    # 初始化
    # arr = []
    # arr = ['physics', 'chemistry', 1997, 2000]

    arr = [0, 1, 2, 3, 4, 5, 6, 7]
    print("arr:", arr)  # 第一项

    # 读取
    print("arr[0]:", arr[0])  # 第一项
    print("arr[-1]:", arr[-1])  # 倒数第一项
    print("arr[2:4]:", arr[2:4])  # 下标2 - 下标4之前
    print("arr[2:-3]:", arr[2:-3])  # 下标2 - 倒数第3下标之前
    print("arr[:4]:", arr[:4])  # 开始 - 下标4之前
    print("arr[:-3]:", arr[:-3])  # 开始 - 倒数第3下标之前
    print("arr[5:]:", arr[5:])  # 下标5 - 结束
    print("arr[-3:]:", arr[-3:])  # 倒数第3下标 - 结束
    print("arr[4:2]:", arr[4:2])  # 头尾错误将返回[]
    # print("arr[[2,3,5]]:", arr[[2, 3, 5]])  # 不支持取特定index，(numpy.array 支持)
    print()

    arr = [[0, 1], [2, 3], [4, 5]]
    print("arr:", arr)
    print("arr[2][1]:", arr[2][1])
    print()


def array_modify():
    print("----------array_modify-----------")

    arr = [0, 1, 2, 3, 4, 5, 6, 7]
    print("arr:", arr)

    # 尾部插入
    arr.append(8)
    print("append arr:", arr)

    # 指定位置插入 原位置后移
    arr.insert(4, 9)
    print("insert (4, 9) arr:", arr)

    # 指定位置插入 若index超出array长度，将在结尾插入
    arr.insert(12, 10)
    print("insert (12, 10) arr:", arr)

    # 删除指定位置 后部分前移

    del arr[1]  # index超出 抛出IndexError
    print("del arr[1] arr:", arr)
    arr.pop(1)  # index超出 抛出IndexError
    print("pop(1) arr:", arr)

    # 翻转
    arr.reverse()
    print("reverse arr:", arr)

    # 转元组  元组将不可修改
    var_tuple = tuple(arr)
    print("var_tuple:", var_tuple)
    print("type(var_tuple):", type(var_tuple))

    # 合并 2个array  调用放将被扩充
    arr2 = [22, 33, 44]
    arr.extend(arr2)
    print("arr:", arr)


def _dict():
    """
    类似于Java Map
    :return: 
    """
    # 不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
    dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
    print("dict:", dict)
    
    # 读
    print("dict['Name']:", dict['Name'])
    print()
    
    # 遍历 key方式
    for key in dict.keys():
        print("dict[%s]:" % key, dict[key])
        
    # 遍历 元组方式
    for tuple_item in dict.items():
        print(tuple_item)

    dict['Age'] = 8  # 更新
    dict['School'] = "RUNOOB"  # 添加
    del dict['Name']  # 删除键是'Name'的条目
    dict.clear()  # 清空字典所有条目 后续再读将抛出KeyError: 'Age'
    del dict  # 删除字典   后续再读将抛出 UnboundLocalError: local variable 'dict' referenced before assignment
    # dict['Age']

    


if __name__ == '__main__':
    # array()
    # array_modify()
    _dict()
