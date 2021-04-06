# -*- coding: utf-8 -*-
# @Time    : 2021/4/5 22:26
# @Author  : Hanxun Yu
# @Email   : 
# @File    : device_helper.py
# @Software: PyCharm
import platform


class EOperationSystem:
    LINUX = 'Linux'
    MAC = 'Darwin'
    WINDOWS = 'Windows'
    OTHER = 'other'


def getOS() -> EOperationSystem:
    os = platform.system()
    if os == EOperationSystem.LINUX:
        return EOperationSystem.LINUX
    elif os == EOperationSystem.MAC:
        return EOperationSystem.MAC
    elif os == EOperationSystem.WINDOWS:
        return EOperationSystem.WINDOWS
    else:
        return EOperationSystem.OTHER


if __name__ == '__main__':
    print(getOS())
