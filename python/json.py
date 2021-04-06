# -*- coding: utf-8 -*-
# @Time    : 2021/4/6 14:06
# @Author  : Han-xun Yu
# @Email   : yuhanxun@126.com
# @File    : json
# @Software: PyCharm

"""
json serialize unserialize
"""
import json


class Person:

    def __init__(self) -> None:
        super().__init__()
        self.name = "haha"
        self.age = 20


def to_json(obj):
    return json.dumps(obj, default=lambda o: o.__dict__,
                      sort_keys=True, indent=4)


def from_json(emptyInstanceObj, jsonStr):
    dict = json.loads(jsonStr)
    emptyInstanceObj.__dict__.update(dict)
    return emptyInstanceObj


if __name__ == '__main__':
    # to json
    p = Person()
    jsonStr = to_json(p)
    print("jsonStr %s" % jsonStr)

    # new instance
    # mod name and age
    p2 = Person()
    p2.name = "aa"
    p2.age = 10
    print("before from json:", to_json(p2))

    # use json str update the obj
    from_json(p2, jsonStr)
    print("after from json:", to_json(p2))
