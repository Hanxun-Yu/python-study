# -*- coding: utf-8 -*-
# @Time    : 2021/2/18 11:25
# @Author  : Han-xun Yu
# @Email   : yuhanxun@126.com
# @File    : console
# @Software: PyCharm

"""

"""


def _print():
    """
    %s    字符串 (采用str()的显示)
    %r    字符串 (采用repr()的显示)
    %c    单个字符
    %b    二进制整数
    %d    十进制整数
    %i    十进制整数
    %o    八进制整数
    %x    十六进制整数
    %e    指数 (基底写为e)
    %E    指数 (基底写为E)
    %f    浮点数
    %F    浮点数，与上相同
    %g    指数(e)或浮点数 (根据显示长度)
    %G    指数(E)或浮点数 (根据显示长度)
    %%    字符"%"
    """

    # 不换行 指定end=""
    print("content", end="")
    print()

    # 格式化
    print("My name is %s and weight is %d kg!" % ('Zara', 29))
    print("{} {}".format("hello", "world"))
    print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))

    # 需要输出%时 使用%%
    print("boolean true %%d:%d" % True)
    print("boolean true %%s:%s" % True)

    # 数字格式化
    print('----------数字格式化----------')
    print('2进制 {:b}'.format(11))
    print('10进制 {:d}'.format(11))
    print('8进制 {:o}'.format(11))
    print('16进制 {:x}'.format(11))
    print('16进制0x开头 小写 {:#x}'.format(11))
    print('16进制0x开头 大写 {:#X}'.format(11))

    print("保留2位小数 {:.2f}".format(3.1415926))
    print("保留2位小数 转% {:.2%}".format(0.25))
    print("科学计数法 " + format(0.0015, '.2e'), " 1.5*10^-3")


if __name__ == '__main__':
    _print()
