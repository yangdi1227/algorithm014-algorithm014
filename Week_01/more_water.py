# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     more_water
   Description :
   Author :       deanyang
   date：          2020/8/13
-------------------------------------------------
   Change Activity:
                   2020/8/13:
-------------------------------------------------
"""
__author__ = 'deanyang'


def main():
    array = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    maxResult = 0
    for i in xrange(0, len(array) - 1):
        for j in xrange(i + 1, len(array)):
            area = (j - i) * min(array[i], array[j])
            maxResult = max(area, maxResult)
    print maxResult


if __name__ == "__main__":
    main()
