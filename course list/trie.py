#!/usr/bin/env python3

class TrieNode:
    # Init the data structure here
    def __init__(self):
        self.val = None
        # pointers is a dictionary
        self.pointers = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # @param {array} words
    # @return {void}
    # Inserts a word into the trie
    def insert(self, words):
        for word in words:
            self.rec_insert(word, self.root)
        return

    def rec_insert(self, word, node):
        if word[:1] not in node.pointers:
            newNode = TrieNode()
            newNode.val = word[:1]
            node.pointers[word[:1]] = newNode
            self.rec_insert(word, node)
        else:
            nextNode = node.pointers[word[:1]]
            if len(word[1:]) == 0:
                nextNode.pointers[' '] = '__END__'
                return
            return self.rec_insert(word[1:], nextNode)

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie
    def search(self, word):
        if len(word) == 0:
            return False
        return self.rec_search(word,self.root)

    def rec_search(self, word, node):
        if word[:1] not in node.pointers:
            return False
        else:
            nextNode = node.pointers[word[:1]]
            if len(word[1:]) == 0:
                if ' ' in nextNode.pointers:
                    return True
                else:
                    return False
            return self.rec_search(word[1:], nextNode)

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie that starts with the given prefix
    def startsWith(self, prefix):
        if len(prefix) == 0:
            return True
        return self.rec_search_prefix(prefix, self.root)

    def rec_search_prefix(self, word, node):
        if word[:1] not in node.pointers:
            return False
        else:
            if len(word[1:])==0:
                return True
            nextNode = node.pointers[word[:1]]
            return self.rec_search_prefix(word[1:], nextNode)

    # @param {Trie} tree
    # @return {void}
    # Print the whole tree
    def pretty_print(self):
        if self == None:
            print('Error: wrong output function')
        else:
            pass
