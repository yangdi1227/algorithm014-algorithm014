# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     firstuniqChar
   Description :
   Author :       deanyang
   date：          2020/10/22
-------------------------------------------------
   Change Activity:
                   2020/10/22:
-------------------------------------------------
"""
__author__ = 'deanyang'

import collections


class Solution:
    def firstUniqChar(self, s) :
        """
        :type s: str
        :rtype: int
        """
        # build hash map : character and how often it appears
        count = collections.Counter(s)

        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1
