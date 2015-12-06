class Trie:
    def __init__(self):
        self.root = None
        self._end = '_end_'

    def build_trie(self, keys, values):
        root = dict()
        size = len(keys)
        for i in range(0, size):
            curr_dict = root
            length = len(keys[i])
            for j in range(0, length):
                curr_dict = curr_dict.setdefault(keys[i][j], {})
            curr_dict[self._end] = values[i]
        self.root = root
        return root

    def compress(self, root):
        new_root = dict()
        curr_dict = root
        for item in curr_dict:
            size = len(curr_dict)
            if item != self._end and size == 1:
                curr_dict[item] = item
                self.compress(item)
        return


    def is_member(self, word):
        curr_dict = self.root
        for letter in word:
            if letter in curr_dict:
                curr_dict = curr_dict[letter]
            else:
                return False
        else:
            if self._end in curr_dict:
                return True
            else:
                return False

    def get(self, word):
        curr_dict = self.root
        for letter in word:
            if letter in curr_dict:
                curr_dict = curr_dict[letter]
            else:
                return False
        else:
            if self._end in curr_dict:
                return curr_dict[self._end]
            else:
                return False


if __name__ == '__main__':
    w = ['foo', 'bar', 'baz', 'barze']
    l = [1, 2, 3, 4]
    t = Trie()
    root = t.build_trie(keys=w, values=l)

    print(t.is_member('foo'))
    print(t.is_member('oof'))

    print(t.get('baz'))
