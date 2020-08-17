# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     is_anagram
   Description :
   Author :       deanyang
   date：          2020/8/17
-------------------------------------------------
   Change Activity:
                   2020/8/17:
-------------------------------------------------
"""
__author__ = 'deanyang'


def main():
    s = 'anagram'
    t = 'nagaram'

    if len(s) != len(t):
        return False

    nums = [0] * 26

    for i in xrange(0, len(s)):
        nums[ord(s[i]) - ord('a')] += 1
        nums[ord(t[i]) - ord('a')] -= 1
    for item in nums:
        if item != 0:
            return False
    return True


if __name__ == "__main__":
    print main()
