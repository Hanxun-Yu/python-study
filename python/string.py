# -*- coding: utf-8 -*-
# @Time    : 2021/2/18 11:20
# @Author  : Han-xun Yu
# @Email   : yuhanxun@126.com
# @File    : string.py
# @Software: PyCharm

"""

"""


def substring(string):
    print("------------substring-------------")

    # 下标切割
    print("string[1:5]:", string[1:5])
    print("string[:5]:", string[:5])

    # 移除头尾<指定字符>
    print("string.strip(\"P\"):", string.strip("P"))
    return


def modify(string):
    print("------------modify-------------")

    # 首字母大写
    print("string.capitalize():", string.capitalize())

    return


def search(src: str, target):
    print("------------search-------------")

    # 遍历
    print('遍历')
    for letter in src:  # 第一个实例
        print(letter, end="")
    print()
    print()

    # 查找，返回index，找不到 抛出异常 ValueError: substring not found
    # print(src.index(target, 0, len(src)))

    # 查找，返回index，找不到 返回-1
    print('find')
    print("find:%d" % src.find(target))  # find start at head
    print("rfind:%d" % src.rfind(target))  # find start at tail
    print(src.find(target, 0, len(src)))
    print()

    # target在src内出现的次数
    print('count')
    print(src.count(target))
    print(src.count(target, 0, len(src)))
    print()

    # startWith  endWith
    print(src + " startswith " + target + " :%s" % src.startswith(target))
    print(src + " endswith " + target + " :%s" % src.endswith(target))


def encode(s, c):
    print("------------encode-------------")
    # ASCII
    print("ASCII")
    ascii = ord(c)
    decode = chr(ascii)
    print("%s:%d" % (c, ascii))
    print("%d:%s" % (ascii, decode))

    print()
    # UTF-8
    print("UTF-8")
    encode = s.encode(encoding='UTF-8', errors='strict')
    decode = encode.decode(encoding='UTF-8', errors='strict')
    print("encode:%s" % encode)
    print("decode:%s" % decode)


if __name__ == '__main__':
    string = "python Runoobp"

    substring(string)
    modify(string)
    search(string, "p")
    encode('abc', 'b')
