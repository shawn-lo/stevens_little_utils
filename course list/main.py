import trie
import numpy as np

t = trie.Trie()
#t.insert('boo')
#t.insert('ball')
#t.insert('boat')
#t.insert('seat')
data = np.array(('boo','ball','boat','seat'))
t.insert(data)
print(t.root.pointers)


