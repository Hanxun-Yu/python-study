# -*- coding: utf-8 -*-
# @Time    : 2021/2/18 16:28
# @Author  : Han-xun Yu
# @Email   : yuhanxun@126.com
# @File    : exception
# @Software: PyCharm

"""

"""


def catch_exception():
    """
        try:
            ...
        except <Exception_1> as ex:
            ...
        except <Exception_2> as ex:
            ...
        finally:
            ...
    """
    try:
        fh = open("testfile", "r")
    # except IOError:  # 简易写法 ，无法读取异常信息
    except IOError as ex:
        print("catch exception:", ex)
        print("Error: 没有找到文件或读取文件失败")
    except Exception as ex:
        print("catch exception:", ex)
        print("未被上面准确捕获，这里使用万能异常捕获")
    finally:
        print("finally")


def catch_exception_2():
    """
            try:
                ...
            except (<Exception_1>, <Exception_2>) as ex:
                ...
            finally:
                ...
        """
    try:
        fh = open("testfile", "r")
    except (IOError, Exception) as ex:
        print("catch exception:", ex)
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
    # throw_exception()
    # catch_exception()
    catch_exception_2()
