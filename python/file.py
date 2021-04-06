# -*- coding: utf-8 -*-
# @Time    : 2021/3/23 17:42
# @Author  : Han-xun Yu
# @Email   : yuhanxun@126.com
# @File    : file_helper.py
# @Software: PyCharm

"""

"""
import os


class FileHelper:
    @staticmethod
    def exists(file_path):
        return os.path.exists(file_path)

    @staticmethod
    def mkdirs(dir_path):
        folder = os.path.exists(dir_path)
        if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs(dir_path)

    @staticmethod
    def mkdirs_parent(file_path):
        FileHelper.mkdirs(os.path.dirname(file_path))

    @staticmethod
    def get_filename(file_path, NeedExt=True):
        fullflname = os.path.split(file_path)[1]
        if NeedExt:
            return fullflname
        else:
            return os.path.splitext(fullflname)[0]

    @staticmethod
    def get_file_ext(file_path):
        fullflname = os.path.split(file_path)[1]
        return os.path.splitext(fullflname)[1]

    @staticmethod
    def get_file_dir(file_path):
        return os.path.split(file_path)[0]

    @staticmethod
    def create_empty_file(file_path):
        FileHelper.mkdirs_parent(file_path)
        fo = open(file_path, "w")
        fo.close()

    @staticmethod
    def write_file(file_path, content):
        fo = open(file_path, "w")
        fo.write(content)
        fo.close()

    @staticmethod
    def read_file(file_path):
        fo = open(file_path, "r")
        data = fo.read()
        fo.close()
        return data


if __name__ == '__main__':
    print("Hello Han-xun Yu")

    path = './dawa/dawd.pg'
    # FileHelper.create_empty_file('./dawa/dawd.pg')
    print(FileHelper.get_filename(path))
    print(FileHelper.get_filename(path, False))
    print(FileHelper.get_file_ext(path))
    print(FileHelper.get_file_dir(path))

    # 获取当前脚本文件路径
    this_pyfile_path = __file__
    print(this_pyfile_path)
