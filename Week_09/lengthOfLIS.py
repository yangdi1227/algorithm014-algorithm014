# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     lengthOfLIS
   Description :
   Author :       deanyang
   date：          2020/10/22
-------------------------------------------------
   Change Activity:
                   2020/10/22:
-------------------------------------------------
"""
__author__ = 'deanyang'


class Solution:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        dp = []
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
