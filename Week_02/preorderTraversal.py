# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     preorderTraversal
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

    def preorderTraversal(self, root):
        #
        if root is None:
            return []
        self.traversal.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)
        return self.traversal


# 迭代
class TreeNode(object):
    """ Definition of a binary tree node."""

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def preorderTraversal(self, root):
        if root is None:
            return []
        stack, output = [root, ], []

        while stack:
            root = stack.pop()
            if root is not None:
                output.append(root.val)
                if root.right is not None:
                    stack.append(root.right)
                if root.left is not None:
                    stack.append(root.left)
        return output
