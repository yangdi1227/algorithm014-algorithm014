# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     rotation
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
    def rotate1(self, nums, k):
        # 暴力求解
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            pass
        else:
            while k > 0:
                a = nums[-1]
                nums[1:n] = nums[0:n - 1]
                nums[0] = a
                k -= 1

    def rotate2(self, nums, k):
        # 反转法
        n = len(nums)
        k %= n
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        # print(nums)
        nums[k:] = nums[k:][::-1]


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7]
    a = Solution()
    # a.rotate1(array, 3)
    a.rotate2(array, 3)
    print array
