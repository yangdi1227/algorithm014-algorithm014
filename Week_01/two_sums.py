# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     two_sums
   Description :
   Author :       deanyang
   date：          2020/8/16
-------------------------------------------------
   Change Activity:
                   2020/8/16:
-------------------------------------------------
"""
__author__ = 'deanyang'


class Solution(object):
    def twoSum1(self, nums, target):
        #暴力法
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) < 2:
            return []
        for i in xrange(0, len(nums) - 1):
            for j in xrange(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j
    def twoSum2(self, nums, target):
        if len(nums) < 2:
            return []
        hashSet = {}
        for i in xrange(0, len(nums)):
            if hashSet.get(target - nums[i]) is not None:
                return [hashSet.get(target - nums[i]), i]
            hashSet[nums[i]] = i


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    a = Solution()
    print a.twoSum2(nums, 9)
