# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     trieNode
   Description :
   Author :       deanyang
   date：          2020/9/28
-------------------------------------------------
   Change Activity:
                   2020/9/28:
-------------------------------------------------
"""
__author__ = 'deanyang'


class TrieNode:

    # Initialize your data structure here.
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            curr = curr.children[c]
        curr.is_word = True

    def search(self, word):
        current = self.root
        for letter in word:
            current = current.children.get(letter)
            if current is None:
                return False
        return current.is_word

    def startsWith(self, prefix):
        current = self.root
        for c in prefix:
            current = current.children.get(c)
            if current is None:
                return False
        return True
