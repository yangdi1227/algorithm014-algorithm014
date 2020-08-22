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
    target = 13

    for index, value in enumerate(nums):
        if d.get(target - value) != None:
            return [d.get(target - value), index]
        d[value] = index


if __name__ == "__main__":
    print main()
