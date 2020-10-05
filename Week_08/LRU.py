# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     LRU
   Description :
   Author :       deanyang
   date：          2020/10/5
-------------------------------------------------
   Change Activity:
                   2020/10/5:
-------------------------------------------------
"""
__author__ = 'deanyang'


# 这句相当于Java的 class LRUCache extend Object {}
# python 里面没有{}，通过缩进来控制代码格式的，而且是强制缩进，
# 如果某一行缩进三个空格，下面一行缩进了四个空间，整个代码就编译不通过
class LRUCache(object):
    # __init__ 就相当于Java的构造函数，def是定义一个函数的意思
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        # 导入python的库函数，python的注释使用#开头的
        import collections
        # self.d 就相当于 Java的 this.d = 。。。
        self.d = collections.OrderedDict()
        self.size = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # 假如key在缓存中，需要先获取到key对应的值，然后删除这个
        # key，再重新插入一遍(插入时会自动放入到第一位)
        if(key in self.d):
            value = self.d[key]
            # del self.d[key] 类似java中的
            # this.d.remove(key)
            del self.d[key]
            self.d[key] = value
            return value
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # 如果key在缓存中，需要先将这个key删除，最后统一再插入
        if(key in self.d):
            del self.d[key]
        # 如果key不在缓存中，那么检查缓存是否满了
        # len(self.d) 相当于Java的 this.d.length
        # 如果满了就删掉最久没用过的那个元素
        else:
            if(len(self.d)==self.size):
                self.d.popitem(False)
        # 最后统一插入这个元素
        self.d[key] = value
