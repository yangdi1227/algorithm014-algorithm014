# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     groupAnagrams
   Description :
   Author :       deanyang
   date：          2020/8/22
-------------------------------------------------
   Change Activity:
                   2020/8/22:
-------------------------------------------------
"""
__author__ = 'deanyang'


def main(nums):
   print groupAnagrams(nums)

def groupAnagrams(nums):
    d = {}
    if not nums:
        return {}
    for item in nums:
        if d.has_key(tuple(sorted(item))):
            d[tuple(sorted(item))].append(item)
        else:
            d[tuple(sorted(item))] = [item]
    return d

if __name__ == "__main__":
    nums = ["eat", "tea", "tan", "ate", "nat", "bat"]
    main(nums)
