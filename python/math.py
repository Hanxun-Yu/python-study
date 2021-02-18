# -*- coding: utf-8 -*-
# @Time    : 2021/2/18 15:46
# @Author  : Han-xun Yu
# @Email   : yuhanxun@126.com
# @File    : math
# @Software: PyCharm

"""

"""


def _round():
    """
    四舍五入
    （注）该函数对于返回的浮点数并不是按照四舍五入的规则来计算
    而会收到计算机表示精度的影响
    
    (总结)
    在用round()函数进行四舍五入时，如果你对结果有十足把握，并且这就是你想要的结果，
    那就放心大胆地使用。不然就老老实实写个函数来实现吧，这不是什么难事。
    :return: 
    """
    print("--------round---------")
    print("round(2.3) :", round(2.3))
    print("round(2.6) :", round(2.6))

    # x.6 正常
    print("round(2.125, 2) :", round(2.126, 2))
    print("round(2.135, 2) :", round(2.136, 2))
    print("round(2.145, 2) :", round(2.146, 2))

    """
    原因是：round()函数不指定位数的时候，返回一个整数，而且是最靠近的整数（类似于四舍五入）
    当指定取舍的小数点位数的时候，一般情况也是使用四舍五入的规则，
    但是碰到.5的情况时，如果要取舍的位数前的小数是奇数，则直接舍弃，如果是偶数则向上取舍。
    
    round()对浮点数的取舍遵循的是“四舍六入五平分”，
    “五平分”就是根据取舍的位数前的小数奇偶性来判断，奇偶平分，符合公平性原则（四舍五入不是公平的），
    这样一来也就保证了在数据量较大的情况下，筛选数据的真实性。
    """
    # x.5 失败
    print("round(2.5) 错:", round(2.5))
    print("round(2.125, 2) 错 :", round(2.125, 2))
    print("round(2.135, 2) 错 :", round(2.135, 2))
    print("round(2.145, 2) 对:", round(2.145, 2))


def integer():
    """
    取整
    :return: 
    """

    import math

    # 向上取整
    print("math.ceil(3.5):", math.ceil(3.5))

    # 向下取整
    print("math.floor(3.4):", math.floor(3.4))

    # 截断取整
    print("math.trunc(3.5):", math.trunc(3.5))


if __name__ == '__main__':
    # _round()
    integer()
