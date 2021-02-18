# -*- coding: utf-8 -*-
# @Time    : 2021/2/18 16:28
# @Author  : Han-xun Yu
# @Email   : yuhanxun@126.com
# @File    : exception
# @Software: PyCharm

"""

"""


def catch_exception():
    try:
        fh = open("testfile", "r")
    
    # except IOError:  # 简易写法 ，无法读取异常信息
    except IOError as e: 
        print("catch exception:", e)
        print("Error: 没有找到文件或读取文件失败")
    finally:
        print("finally")


def throw_exception():
    try:
        # 抛出异常
        raise Exception("Error")
    except Exception as e:
        print("catch exception:", e)
    finally:
        print("finally")


if __name__ == '__main__':
    catch_exception()
