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

#组合（微软、亚马逊、谷歌在半年内面试中考过）
class Solution(object):
    def combine(self, n, k):
        def backtrack(first=1, curr=[]):
            # if the combination is done
            if len(curr) == k:
                output.append(curr[:])
                return
            for i in range(first, n + 1):
                # add i into the current combination
                curr.append(i)
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack，这一步不是很明白，为什么要pop
                # 清理现场，因为你的回溯的过程中，会残留老的curr的脏数据
                curr.pop()

        output = []
        backtrack()
        return output


if __name__ == '__main__':
    a = Solution()
    print a.combine(4, 2)
