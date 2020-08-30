# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     lowestCommonAncestor
   Description :
   Author :       deanyang
   date：          2020/8/30
-------------------------------------------------
   Change Activity:
                   2020/8/30:
-------------------------------------------------
"""
__author__ = 'deanyang'


class TreeNode(object):
    """ Definition of a binary tree node."""

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowest_common_ancestor(self, root, p, q):
        if not root or root == p or root == q: return root
        left = self.lowest_common_ancestor(root.left, p, q)
        right = self.lowest_common_ancestor(root.right, p, q)
        if not left: return right
        if not right: return left
        return root
