# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     inorderTraversal
   Description :
   Author :       deanyang
   date：          2020/8/23
-------------------------------------------------
   Change Activity:
                   2020/8/23:
-------------------------------------------------
"""
__author__ = 'deanyang'


# 递归
class Solution(object):
    def __init__(self):
        self.traversal = []

    def inorderTraversal(self, root):
        if root is None:
            return []
        self.inorderTraversal(root.left)
        self.traversal.append(root.val)
        self.inorderTraversal(root.right)
        return self.traversal


# 迭代
class Solution:
    def inorderTraversal(self, root):
        res = []
        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            top = stack.pop() #此时左子树遍历完成
            res.append(top.val)  #将父节点加入列表
            cur = top.right #遍历右子树
        return res

