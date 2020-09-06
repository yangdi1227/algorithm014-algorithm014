# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     lemonadeChange
   Description :
   Author :       deanyang
   date：          2020/9/6
-------------------------------------------------
   Change Activity:
                   2020/9/6:
-------------------------------------------------
"""
__author__ = 'deanyang'


class Solution(object): #aw
    def lemonadeChange(self, bills):
        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if not five: return False
                ten += 1
                five -= 1
            else:
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        print five,ten
        return True

if __name__ == "__main__":
     change = [5,5,5,15]
     a = Solution()
     print a.lemonadeChange(change)
