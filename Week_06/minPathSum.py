# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     minPathSum
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
    def minPathSum(self, grid):
        if not grid or not grid[0]:
            return 0

        rows, columns = len(grid), len(grid[0])
        dp = [[0] * columns for _ in range(rows)]
        dp[0][0] = grid[0][0]
        for i in range(1, rows):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, columns):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(1, rows):
            for j in range(1, columns):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[rows - 1][columns - 1]
