# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     removeDuplicates
   Description :
   Author :       deanyang
   date：          2020/8/15
-------------------------------------------------
   Change Activity:
                   2020/8/15:
-------------------------------------------------
"""
__author__ = 'deanyang'


def main():
    array = [1,1,2]
    print solution1(array)


# 1. 双指针
def solution1(array):
    if not array:
        return 0
    if len(array) == 1:
        return 1
    i = 0

    for j in xrange(1, len(array)):
        if array[i] != array[j]:
            array[i + 1] = array[j]
            i += 1
    return i + 1,array


if __name__ == "__main__":
    main()
