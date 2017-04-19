# practicing trie implementation
# using the implementation provided by Steve Hanov -- just adding
# personal comments

# Trie data structure keeps a set of words, organized with one node
# per letter.  Each node has branch for each letter that may follow
# in set of words.

# e.g., if SET OF WORDS includes
# short, shirt, shorter, shortest, shirts
# Trie would look like... ?
#                       - s - t
# s - h - o - r - t - e - r
#       - i - r - t - s
        
class TrieNode:
    def __init__(self):
        self.word = None
        self.children = {}
        
    def insert(self, word):
        node = self
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.word = word

