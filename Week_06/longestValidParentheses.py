# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     longestValidParentheses
   Description :
   Author :       deanyang
   date：          2020/9/20
-------------------------------------------------
   Change Activity:
                   2020/9/20:
-------------------------------------------------
"""
__author__ = 'deanyang'

class Solution:
    def longestValidParentheses(self, s):
        n = len(s)
        if n == 0: return 0
        dp = [0] * n
        res = 0
        for i in range(n):
            if i>0 and s[i] == ")":
                if  s[i - 1] == "(":
                    dp[i] = dp[i - 2] + 2
                elif s[i - 1] == ")" and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":
                    dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
                if dp[i] > res:
                    res = dp[i]
        return res
