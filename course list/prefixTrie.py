#! usr/bin/env python3

class TrieNode:
    def __init__(self):
        self.val = None
        self.children={}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    def insert(self, *words):
        if len(words) == 0:
            print('Error: The words don\'t exist.')
            return
        for word in words:
            pass
    def recursive_insert(self, word, node)

