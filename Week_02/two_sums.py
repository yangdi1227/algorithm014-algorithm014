# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     two_sums
   Description :
   Author :       deanyang
   date：          2020/8/20
-------------------------------------------------
   Change Activity:
                   2020/8/20:
-------------------------------------------------
"""
__author__ = 'deanyang'


def main():
    nums = [2, 7, 11, 15]
    d = dict()
    target = 9

    for index, value in enumerate(nums):
        if d.get(value) == None:
            d[target - value] = index
        else:
            return [d.get(value), index]


if __name__ == "__main__":
    print main()
