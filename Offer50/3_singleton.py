""" [单例模式](https://www.lintcode.com/problem/singleton/description?_from=ladder&&fromId=6)
单例 是最为最常见的设计模式之一。对于任何时刻，如果某个类只存在且最多存在一个具体的实例，那么我们称这种设计模式为单例。例如，对于 class Mouse (不是动物的mouse哦)，我们应将其设计为 singleton 模式。
你的任务是设计一个 getInstance 方法，对于给定的类，每次调用 getInstance 时，都可得到同一个实例。

PS: 在 LintCode 上是以修改 __new__方法
"""
import abc
import functools


# 修改 __new__ 方法
class Solution:
    instances = None

    def __new__(cls, *args, **kwargs):
        if not cls.instances:
            cls.instances = Solution(*args, **kwargs)
        return cls.instances


# 类装饰器
def singleton(c, *args, **kwargs):
    instances = []

    @functools.wraps(c)
    def decorator():
        if c not in instances:
            instances[c] = c(*args, **kwargs)
        return instances[c]

    return decorator


# 元类法
class Singleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance


class MyClass(metaclass=Singleton):
    pass


# 使用共享属性
class Singleton2:
    __dict__ = []

    def __init__(self):
        self.__dict__ = __dict__
