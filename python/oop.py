# -*- coding: utf-8 -*-
# @Time    : 2021/2/18 16:15
# @Author  : Han-xun Yu
# @Email   : yuhanxun@126.com
# @File    : oop
# @Software: PyCharm

"""

"""


class Employee:
    # 类变量（所有对象共享 类似java static）
    empCount = 0

    def __init__(self, name, salary):
        # 成员变量 self.xxx
        self.name = name
        self.salary = salary
        self.__private_attr = 10
        self._protected_attr = 10
        Employee.empCount += 1

    def __private_fun(self):
        """
        私有成员函数
        :return: 
        """
        print("call _private_fun()")

    def _protected_fun(self):
        """
       protected成员函数
       :return: 
       """
        print("call _protected_fun()")

    def display_count(self):
        print("Total Employee %d" % Employee.empCount)

    def display_employee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


if __name__ == '__main__':
    # 实例化
    emp1 = Employee("Zara", 2000)

    # 调用对象函数
    emp1.display_employee()

    # 类属性
    print(Employee.empCount)

    # 类属性 通过对象访问
    print(emp1.empCount)

    # 对象属性
    print(emp1.name)

    # 失败 访问私有成员变量 将异常
    # print(emp1.__private_attr)

    # 失败 访问私有成员函数 将异常
    # print(emp1.__private_fun())

    # 警告 访问protected属性
    print(emp1._protected_attr)

    # 警告 访问protected函数
    emp1._protected_fun()

    print("type(emp1):", type(emp1))
