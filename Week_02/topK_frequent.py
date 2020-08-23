# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     topK_frequent
   Description :
   Author :       deanyang
   date：          2020/8/23
-------------------------------------------------
   Change Activity:
                   2020/8/23:
-------------------------------------------------
"""
import heapq
import collections
__author__ = 'deanyang'


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        dic = collections.Counter(nums)
        queue = []
        res = []
        for i in dic:
            heapq.heappush(queue, (-dic[i], i))
        for i in range(k):
            tmp = heapq.heappop(queue)
            res.append(tmp[1])
        return res

if __name__ == '__main__':
    nums = ['a','a','a','b','c','c','d',]
    a = Solution()
    print a.topKFrequent(nums, 2)

