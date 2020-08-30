# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     combine
   Description :
   Author :       deanyang
   date：          2020/8/30
-------------------------------------------------
   Change Activity:
                   2020/8/30:
-------------------------------------------------
"""
__author__ = 'deanyang'


class Solution(object):
    def combine(self, n, k):
        def backtrack(first=1, curr=[]):
            # if the combination is done
            if len(curr) == k:
                output.append(curr[:])
            for i in range(first, n + 1):
                # add i into the current combination
                curr.append(i)
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack，这一步不是很明白，为什么要pop
                curr.pop()

        output = []
        backtrack()
        return output


if __name__ == '__main__':
    a = Solution()
    print a.combine(4, 2)
