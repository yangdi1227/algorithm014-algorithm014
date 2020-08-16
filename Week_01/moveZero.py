# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     moveZero
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
    array_src = [0, 1, 3, 0, 2]
    j = 0
    print array_src
    for i in xrange(0, len(array_src)):
        if array_src[i] != 0:
            array_src[j] = array_src[i]
            # if i != j:
            #     array_src[i] = 0
            j += 1
        print array_src


if __name__ == "__main__":
    main()
