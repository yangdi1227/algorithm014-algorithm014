# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     hammingWeight
   Description :
   Author :       deanyang
   date：          2020/10/5
-------------------------------------------------
   Change Activity:
                   2020/10/5:
-------------------------------------------------
"""
__author__ = 'deanyang'

class Solution:
    def hammingWeight(self, n):

        ans = 0

        while n > 0:

            ans += n & 1

            n >>= 1

        return ans
