# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     NTree-preorder
   Description :
   Author :       deanyang
   date：          2020/8/22
-------------------------------------------------
   Change Activity:
                   2020/8/22:
-------------------------------------------------
"""
__author__ = 'deanyang'


class Solution:
    def __init__(self):
        self.traversal = []

    def preopder_recursion(self, root):
        self.preOrder0(root)
        return self.traversal

    def preOrder0(self, node):
        # 递归
        if node is None:
            return []
        self.traversal.append(node.val)
        for child in node.children:
            self.preOrder0(child)

    def preorder_iteration(self, root):
        # 迭代
        if root is None:
            return []
        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            stack.extend(root.children[::-1])
        return output


if __name__ == "__main__":
    pass
