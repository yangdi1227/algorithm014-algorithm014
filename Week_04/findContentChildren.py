# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     findContentChildren
   Description :
   Author :       deanyang
   date：          2020/9/6
-------------------------------------------------
   Change Activity:
                   2020/9/6:
-------------------------------------------------
"""
__author__ = 'deanyang'


class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        res = 0
        g.sort()
        s.sort()
        g_length = len(g)
        s_length = len(s)

        i = j = 0

        while i < g_length and j < s_length:
            if g[i] < s[j]:
                res += 1
                i += 1
                j += 1
            else:
                j += 1
        return res